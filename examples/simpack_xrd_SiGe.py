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
# Copyright (c) 2016-2023 Dominik Kriegner <dominik.kriegner@gmail.com>

from numpy import inf, linspace, mean, pi, sqrt
from matplotlib.pylab import (clf, figure, legend, mpl, semilogy, show,
                              tight_layout, vlines, xlabel, xlim, ylabel)

import xrayutilities as xu

mpl.rcParams['font.size'] = 16.0


en = 8500  # eV
resol = 0.0004  # resolution in q
H, K, L = (0, 0, 4)
qz = linspace(4.2, 5.0, 3000)

sub = xu.simpack.Layer(xu.materials.Si, inf)
lay = xu.simpack.Layer(xu.materials.SiGe(0.6), 145.87, relaxation=0.5)
# pseudomorphic stack -> adjusts lattice parameters!
pls = xu.simpack.PseudomorphicStack001('pseudo', sub, lay)

# calculate incidence angle for dynamical diffraction models
qx = sqrt(sub.material.Q(H, K, L)[0]**2 + sub.material.Q(H, K, L)[1]**2)
ai = xu.simpack.coplanar_alphai(qx, qz, en)
resolai = abs(xu.simpack.coplanar_alphai(qx, mean(qz) + resol, en) -
              xu.simpack.coplanar_alphai(qx, mean(qz), en))

# comparison of different diffraction models
# simplest kinematical diffraction model
mk = xu.simpack.KinematicalModel(pls, energy=en, resolution_width=resol)
Ikin = mk.simulate(qz, hkl=(H, K, L), refraction=True)

# kinematic multibeam diffraction model
mk = xu.simpack.KinematicalMultiBeamModel(pls, energy=en,
                                          surface_hkl=(0, 0, 1),
                                          resolution_width=resol)
Imult = mk.simulate(qz, hkl=(H, K, L), refraction=True)

# simplified dynamical diffraction model
mds = xu.simpack.SimpleDynamicalCoplanarModel(pls, energy=en,
                                              resolution_width=resolai)
Idynsub = mds.simulate(ai, hkl=(H, K, L), idxref=0)
Idynlay = mds.simulate(ai, hkl=(H, K, L), idxref=1)

# general 2-beam theory based dynamical diffraction model
md = xu.simpack.DynamicalModel(pls, energy=en, resolution_width=resolai)
Idyn = md.simulate(ai, hkl=(H, K, L))

# plot of calculated intensities
figure('XU-simpack SiGe')
clf()
semilogy(qz, Ikin, label='kinematical')
semilogy(qz, Imult, label='multibeam')
semilogy(xu.simpack.get_qz(qx, ai, en), Idynsub, label='simpl. dynamical(S)')
semilogy(xu.simpack.get_qz(qx, ai, en), Idynlay, label='simpl. dynamical(L)')
semilogy(xu.simpack.get_qz(qx, ai, en), Idyn, label='full dynamical')
vlines([4*2*pi/layer.material.a3[-1] for layer in pls],
       1e-9, 1, linestyles='dashed')
legend(fontsize='small')
xlim(qz.min(), qz.max())
xlabel(r'Qz ($1/\mathrm{\AA}$)')
ylabel('Intensity (arb. u.)')
tight_layout()
show()
