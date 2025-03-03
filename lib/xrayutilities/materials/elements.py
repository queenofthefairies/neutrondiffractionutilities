# This file is part of xrayutilities.
#
# xrayutilities is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.
#
# Copyright (C) 2009 Eugen Wintersberger <eugen.wintersberger@desy.de>
# Copyright (C) 2010-2025 Dominik Kriegner <dominik.kriegner@gmail.com>

from .atom import Atom

Dummy = Atom('Dummy', 0)
H = Atom('H', 1)
Hdot = Atom('H.', 1)
H1m = Atom('H1-', 1)
D = Atom('D', 1)
T = Atom('T', 1)
He = Atom('He', 2)
Li = Atom('Li', 3)
Li1p = Atom('Li1+', 3)
Be = Atom('Be', 4)
Be2p = Atom('Be2+', 4)
B = Atom('B', 5)
C = Atom('C', 6)
Cdot = Atom('C.', 6)
N = Atom('N', 7)
O = Atom('O', 8)  # noqa: E741
O1m = Atom('O1-', 8)
O2mdot = Atom('O2-.', 8)
O2m = Atom('O2-.', 8)
F = Atom('F', 9)
F1m = Atom('F1-', 9)
Ne = Atom('Ne', 10)
Na = Atom('Na', 11)
Na1p = Atom('Na1+', 11)
Mg = Atom('Mg', 12)
Mg2p = Atom('Mg2+', 12)
Al = Atom('Al', 13)
Al3p = Atom('Al3+', 13)
Si = Atom('Si', 14)
Sidot = Atom('Si.', 14)
Si4p = Atom('Si4+', 14)
P = Atom('P', 15)
S = Atom('S', 16)
Cl = Atom('Cl', 17)
Cl1m = Atom('Cl1-', 17)
Ar = Atom('Ar', 18)
K = Atom('K', 19)
K1p = Atom('K1+', 19)
Ca = Atom('Ca', 20)
Ca2p = Atom('Ca2+', 20)
Sc = Atom('Sc', 21)
Sc3p = Atom('Sc3+', 21)
Ti = Atom('Ti', 22)
Ti2p = Atom('Ti2+', 22)
Ti3p = Atom('Ti3+', 22)
Ti4p = Atom('Ti4+', 22)
V = Atom('V', 23)
V2p = Atom('V2+', 23)
V3p = Atom('V3+', 23)
V5p = Atom('V5+', 23)
Cr = Atom('Cr', 24)
Cr2p = Atom('Cr2+', 24)
Cr3p = Atom('Cr3+', 24)
Mn = Atom('Mn', 25)
Mn2p = Atom('Mn2+', 25)
Mn3p = Atom('Mn3+', 25)
Mn4p = Atom('Mn4+', 25)
Fe = Atom('Fe', 26)
Fe2p = Atom('Fe2+', 26)
Fe3p = Atom('Fe3+', 26)
Co = Atom('Co', 27)
Co2p = Atom('Co2+', 27)
Co3p = Atom('Co3+', 27)
Ni = Atom('Ni', 28)
Ni2p = Atom('Ni2+', 28)
Ni3p = Atom('Ni3+', 28)
Cu = Atom('Cu', 29)
Cu1p = Atom('Cu1+', 29)
Cu2p = Atom('Cu2+', 29)
Zn = Atom('Zn', 30)
Zn2p = Atom('Zn2+', 30)
Ga = Atom('Ga', 31)
Ga3p = Atom('Ga3+', 31)
Ge = Atom('Ge', 32)
Ge4p = Atom('Ge4+', 32)
As = Atom('As', 33)
Se = Atom('Se', 34)
Br = Atom('Br', 35)
Br1m = Atom('Br1-', 35)
Kr = Atom('Kr', 36)
Rb = Atom('Rb', 37)
Rb1p = Atom('Rb1+', 37)
Sr = Atom('Sr', 38)
Sr2p = Atom('Sr2+', 38)
Y = Atom('Y', 39)
Y3p = Atom('Y3+', 39)
Zr = Atom('Zr', 40)
Zr4p = Atom('Zr4+', 40)
Nb = Atom('Nb', 41)
Nb3p = Atom('Nb3+', 41)
Nb5p = Atom('Nb5+', 41)
Mo = Atom('Mo', 42)
Mo3p = Atom('Mo3+', 42)
Mo5p = Atom('Mo5+', 42)
Mo6p = Atom('Mo6+', 42)
Tc = Atom('Tc', 43)
Ru = Atom('Ru', 44)
Ru3p = Atom('Ru3+', 44)
Ru4p = Atom('Ru4+', 44)
Rh = Atom('Rh', 45)
Rh3p = Atom('Rh3+', 45)
Rh4p = Atom('Rh4+', 45)
Pd = Atom('Pd', 46)
Pd2p = Atom('Pd2+', 46)
Pd4p = Atom('Pd4+', 46)
Ag = Atom('Ag', 47)
Ag1p = Atom('Ag1+', 47)
Ag2p = Atom('Ag2+', 47)
Cd = Atom('Cd', 48)
Cd2p = Atom('Cd2+', 48)
In = Atom('In', 49)
In3p = Atom('In3+', 49)
Sn = Atom('Sn', 50)
Sn2p = Atom('Sn2+', 50)
Sn4p = Atom('Sn4+', 50)
Sb = Atom('Sb', 51)
Sb3p = Atom('Sb3+', 51)
Sb5p = Atom('Sb5+', 51)
Te = Atom('Te', 52)
I = Atom('I', 53)  # noqa: E741
I1m = Atom('I1-', 53)
Xe = Atom('Xe', 54)
Cs = Atom('Cs', 55)
Cs1p = Atom('Cs1+', 55)
Ba = Atom('Ba', 56)
Ba2p = Atom('Ba2+', 56)
La = Atom('La', 57)
La3p = Atom('La3+', 57)
Ce = Atom('Ce', 58)
Ce3p = Atom('Ce3+', 58)
Ce4p = Atom('Ce4+', 58)
Pr = Atom('Pr', 59)
Pr3p = Atom('Pr3+', 59)
Pr4p = Atom('Pr4+', 59)
Nd = Atom('Nd', 60)
Nd3p = Atom('Nd3+', 60)
Pm = Atom('Pm', 61)
Pm3p = Atom('Pm3+', 61)
Sm = Atom('Sm', 62)
Sm3p = Atom('Sm3+', 62)
Eu = Atom('Eu', 63)
Eu2p = Atom('Eu2+', 63)
Eu3p = Atom('Eu3+', 63)
Gd = Atom('Gd', 64)
Gd3p = Atom('Gd3+', 64)
Tb = Atom('Tb', 65)
Tb3p = Atom('Tb3+', 65)
Dy = Atom('Dy', 66)
Dy3p = Atom('Dy3+', 66)
Ho = Atom('Ho', 67)
Ho3p = Atom('Ho3+', 67)
Er = Atom('Er', 68)
Er3p = Atom('Er3+', 68)
Tm = Atom('Tm', 69)
Tm3p = Atom('Tm3+', 69)
Yb = Atom('Yb', 70)
Yb2p = Atom('Yb2+', 70)
Yb3p = Atom('Yb3+', 70)
Lu = Atom('Lu', 71)
Lu3p = Atom('Lu3+', 71)
Hf = Atom('Hf', 72)
Hf4p = Atom('Hf4+', 72)
Ta = Atom('Ta', 73)
Ta5p = Atom('Ta5+', 73)
W = Atom('W', 74)
W6p = Atom('W6+', 74)
Re = Atom('Re', 75)
Os = Atom('Os', 76)
Os4p = Atom('Os4+', 76)
Ir = Atom('Ir', 77)
Ir3p = Atom('Ir3+', 77)
Ir4p = Atom('Ir4+', 77)
Pt = Atom('Pt', 78)
Pt2p = Atom('Pt2+', 78)
Pt4p = Atom('Pt4+', 78)
Au = Atom('Au', 79)
Au1p = Atom('Au1+', 79)
Au3p = Atom('Au3+', 79)
Hg = Atom('Hg', 80)
Hg1p = Atom('Hg1+', 80)
Hg2p = Atom('Hg2+', 80)
Tl = Atom('Tl', 81)
Tl1p = Atom('Tl1+', 81)
Tl3p = Atom('Tl3+', 81)
Pb = Atom('Pb', 82)
Pb2p = Atom('Pb2+', 82)
Pb4p = Atom('Pb4+', 82)
Bi = Atom('Bi', 83)
Bi3p = Atom('Bi3+', 83)
Bi5p = Atom('Bi5+', 83)
Po = Atom('Po', 84)
At = Atom('At', 85)
Rn = Atom('Rn', 86)
Fr = Atom('Fr', 87)
Ra = Atom('Ra', 88)
Ra2p = Atom('Ra2+', 88)
Ac = Atom('Ac', 89)
Ac3p = Atom('Ac3+', 89)
Th = Atom('Th', 90)
Th4p = Atom('Th4+', 90)
Pa = Atom('Pa', 91)
U = Atom('U', 92)
U3p = Atom('U3+', 92)
U4p = Atom('U4+', 92)
U6p = Atom('U6+', 92)
Np = Atom('Np', 93)
Np3p = Atom('Np3+', 93)
Np4p = Atom('Np4+', 93)
Np6p = Atom('Np6+', 93)
Pu = Atom('Pu', 94)
Pu3p = Atom('Pu3+', 94)
Pu4p = Atom('Pu4+', 94)
Pu6p = Atom('Pu6+', 94)
Am = Atom('Am', 95)
Cm = Atom('Cm', 96)
Bk = Atom('Bk', 97)
Cf = Atom('Cf', 98)
Es = Atom("Es", 99)
Fm = Atom("Fm", 100)
Md = Atom("Md", 101)
No = Atom("No", 102)
Lr = Atom("Lr", 103)
Rf = Atom("Rf", 104)
Db = Atom("Db", 105)
Sg = Atom("Sg", 106)
Bh = Atom("Bh", 107)
Hs = Atom("Hs", 108)
Mt = Atom("Mt", 109)
Ds = Atom("Ds", 110)
Rg = Atom("Rg", 111)
Cn = Atom("Cn", 112)
Uut = Atom("Uut", 113)
Uuq = Atom("Uuq", 114)
Uup = Atom("Uup", 115)
Uuh = Atom("Uuh", 116)
Uus = Atom("Uus", 117)
Uuo = Atom("Uuo", 118)
