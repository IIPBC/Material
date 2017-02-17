# -*- coding:utf-8 -*-

"""
2nd IAG Pyhton Boot Camp

pyFITS tutorial. To be executed preferably in ``ipython`` (with --pylab).
"""
__author__ = "Daniel Moser"
__email__ = "dmfaes@gmail.com"

# Start pyfits
# try:
import pyfits as pf
# except:
# import astropy.io.fits as pf

# Other imports    
import numpy as np
import matplotlib.pyplot as plt

# write below the data directory path
path = './data/'

# See spec
imname = path+'spec.fits'
# open file
hdulist = pf.open(imname)
print( hdulist.info() )
hdulist.close()
# (input) stop
#~ raw_input('# Type ENTER to continue...')


# Reading the file this time:
hdulist = pf.open(imname)
# Assigning header + data
prihdr = hdulist[0].header  # get first Table header
pridata = hdulist[0].data   # get first Table data
# In an alternative way
spechdr = pf.getheader(imname, 0)  # get first Table header
specdata = pf.getdata(imname, 0)  # get first Table data
# In a more direct way
specdata, spechdr = pf.getdata(imname, 0, header=True)
print( np.shape(prihdr), np.shape(spechdr) )
print( np.shape(pridata), np.shape(specdata) )
# closing the file
hdulist.close()
#~ raw_input('# Type ENTER to continue...')


# Looking header...
print( spechdr[:10] )
print( spechdr.cards[:10] )
#~ raw_input('# Type ENTER to continue...')
print( spechdr.keys() )
# Check keyword
print( 'INTTIME' in spechdr )
print( 'EXPTIME' in spechdr )
print( spechdr['EXPTIME'] )
# Building lambda array 
cdelt1 = spechdr['CDELT1']
crval1 = spechdr['CRVAL1']
naxis1 = spechdr['NAXIS1']
lbdarr = np.arange(naxis1)*cdelt1+crval1


# One can add, edit and erase header entries!
spechdr.add_history('IAG PBC example')
print( spechdr.cards[-50:-40] )
# 
keyw = 'OBSERVER'
print( spechdr[keyw] )
spechdr.update(keyw, 'Edwin Hubble')
print( spechdr[keyw] )
# 
print( keyw in spechdr )
spechdr.pop(keyw)
print( keyw in spechdr )
# Caution! You can easily create entries!
# Be sure of the Keyword you are using
spechdr[keyw] = ('Edwin Hubble', 'That guy at the telescope...')
print( keyw in spechdr )


# Accessing table data...
print( specdata.shape )
print( specdata[1000:1050] )
print( np.min(specdata), np.max(specdata) )
# Plotting it
plt.plot(lbdarr, specdata, 'o-', ms=2)
plt.plot(plt.xlim(), [1, 1], '--', color='gray')
plt.show()
#~ raw_input('# Type ENTER to continue...')
# Histogram
plt.clf()
n, bins, patches = plt.hist(specdata)
plt.show()
#~ raw_input('# Type ENTER to continue...')
plt.close()


# Saving = 2 ways. One...
# pf.writeto('spec_modified.fits', specdata, header=spechdr)
# If you already have it...
pf.writeto('spec_modified.fits', specdata, header=spechdr, clobber=True)
# Or...
hdulist = pf.open('spec_modified.fits', mode='update')
# making changes in data and/or header
# ...
hdulist.flush()  # changes are written back to original.fits
hdulist.close()  # closing the file will also flush any changes and ...
# ... prevent further writing


# Loading RBG fits
imname = path+'hdust_rgb.fits'
red = pf.getdata(imname)  # get first Table data
green = pf.getdata(imname, 1)  # get nth Table data
blue = pf.getdata(imname, ext=2)  # get nth Table data
# RGB 8-bits format
out = np.dstack((red, green, blue))
print( np.shape(out) )
RGB = out*255./np.max(out)
# Save it with PIL
import PIL
img = PIL.Image.fromarray(RGB.astype('uint8'))
img.save('hdust_rgb.png')
img.close()


# Creating FITS cube from scratch
red = np.arange(256*256).reshape((256, 256))
green = np.zeros((256, 256))+128
blue = np.random.random(256*256).reshape((256, 256))*256
# Save FITS
new_hdul = pf.HDUList()
new_hdul.append(pf.ImageHDU(data=red))
new_hdul.append(pf.ImageHDU(data=green))
new_hdul.append(pf.ImageHDU(data=blue))
new_hdul.writeto('new_rgb.fits', clobber=True)
# Alternative way - To complete is the challenge!
out = pf.PrimaryHDU()
hdulist2 = pf.HDUList([out])
hdulist2.writeto('new_fits.fits', clobber=True)
# Which are the differences??? (st)


# Accessing Tabular Data
imname = path+'vo_table.fits.gz'
# pyFITS opens compressed FITS!!!
hdu = pf.open(imname)
print( hdu.info() )
print( hdu[0].header )
print( hdu[0].data[:10] )
# From what is this data type???
print( hdu[1].header )
print( hdu[1].data[:10] )
tab = hdu[1].data
print( tab['Name'][:10] )
plt.hist(tab['Vmag'])
