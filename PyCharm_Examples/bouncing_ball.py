#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Create an animation using classes
    and matplotlib.

    by B. Quint
"""
import matplotlib.pyplot as plt
import matplotlib.animation as pani
import numpy as np


def main():

    my_particle_1 = Particle(0.1, 0.001)
    my_particle_2 = Particle(0.2, 0.0025)

    my_box = Box()
    my_box.add_particle(my_particle_1)
    my_box.add_particle(my_particle_2)

    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_axes([0, 0, 1, 1], frameon=False)
    ax.set_xlim(0, 1), ax.set_xticks([])
    ax.set_ylim(0, 1), ax.set_yticks([])

    lines = []
    for p in my_box.list_of_particles:
        line, = ax.plot(p.x, p.y, 'o')
        lines.append(line)

    def update(frame_number):
        """
        Update the plot. Please, note that this
        function is defined **inside** the main
        function.
        """
        my_box.one_interaction()
        for i in range(my_box.n_particles):
            p = my_box.list_of_particles[i]
            lines[i].set_data(p.x, p.y)

    animation = pani.FuncAnimation(fig, update, interval=10)
    plt.show()


class Box:

    def __init__(self):
        """Create one box to put particles"""
        self.limits = [0, 1]
        self.list_of_particles = []
        self.n_particles = len(self.list_of_particles)

    def add_particle(self, particle):
        """Add one partice inside the box."""
        self.list_of_particles.append(particle)
        self.n_particles = len(self.list_of_particles)

    def one_interaction(self):
        """Update the position of the particle."""
        for p in self.list_of_particles:

            x_old = p.x
            p.update()
            x_new = p.x

            if p.x < min(self.limits):
                p.change_direction()
                p.x = min(self.limits) - (x_old - x_new)

            elif p.x > max(self.limits):
                p.change_direction()
                p.x = max(self.limits) - (x_new - x_old)


class Particle:

    def __init__(self, x0, v0):
        """
        Creates a bouncing ball. To make this example
        clear, use x0 between 0 and 1 and v0 between 0.01
        and 0.1.

        Parameters
        ----------
            x0 : float
                Initial position.
            v0 : float
                Velocity.
        """
        self.x = x0
        self.y = np.random.rand()
        self.v = v0

    def __str__(self):
        """This is a string representation."""
        return "x = {:03.2f} - v = {:03.2f}".format(
            self.x, self.v
        )

    def change_direction(self):
        """
        Change the direction of the particle.
        """
        self.v = -self.v

    def update(self):
        """
        Update the position where the particle is.
        """
        # self.x = self.x + self.v
        self.x += self.v  # Increment velocity

if __name__ == "__main__":
    main()
