class Atom:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.type = 1
        self.vx = 0.0
        self.vy = 0.0
        self.vz = 0.0


def get_atoms():
    atoms = []
    r = 4
    s = 1.55
    h = 0.5 * s
    for ix in range(r):
        for iy in range(r):
            for iz in range(r):
                x = ix * s
                y = iy * s
                z = iz * s
                atoms.append(Atom(x, y, z))
                atoms.append(Atom(x, y+h, z+h))
                atoms.append(Atom(x+h, y, z+h))
                atoms.append(Atom(x+h, y+h, z))
    return atoms


def save_file(filename, atoms):
    with open(filename, "w") as f:
        f.write("Position Data\n\n")
        f.write("{} atoms\n".format(len(atoms)))
        f.write("1 atom types\n\n")
        f.write("-40.00 40.00 xlo xhi\n")
        f.write("-20.00 20.00 ylo yhi\n")
        f.write("-20.00 20.00 zlo zhi\n")
        f.write("\n")
        f.write("Atoms\n\n")
        for i, a in enumerate(atoms):
            f.write("{} {} {} {} {}\n".format(i+1, a.type, a.x, a.y, a.z))
        f.write("\n")
        f.write("Velocities\n\n")
        for i, a in enumerate(atoms):
            f.write("{} {} {} {}\n".format(i+1, a.vx, a.vy, a.vz))
    print(f"{len(atoms)} atoms")
    print(f"Generated {filename}")


def find_range(atoms):
    x = []
    y = []
    z = []
    for a in atoms:
        x.append(a.x)
        y.append(a.y)
        z.append(a.z)
    print(f"{min(x)} < x < {max(x)}")
    print(f"{min(y)} < y < {max(y)}")
    print(f"{min(z)} < z < {max(z)}")


if __name__ == "__main__":
    a = get_atoms()
    find_range(a)
    save_file("restart.atoms", a)
