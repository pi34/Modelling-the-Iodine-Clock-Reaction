import scipy

# Initial Concentrations
IO3 = int(input()) # 0.0715
HSO3 = int(input()) # 0.0101
HIO2 = int(input()) # 0
I = int(input()) # 1e-6
H = int(input()) # 8.36e-9
HIO = int(input()) # 0
I2 = int(input()) # 0
SO3 = int(input()) # 0.0764

# Rate Constants
k1 = 2.95e-1
k2 = 2.0e10
k3 = 1.0e5
k4 = 3.0e5
k5 = 3.0e12
k6 = 2.2
k7 = 1.0e6
k8 = 5.0e10
k9 = 3.0e3

# Rate Laws
r1 = k1*IO3*HSO3
r2 = k2*HIO2*I*H
r3 = k3*HIO2*HIO
r4 = k4*IO3*I*H
r5 = k5*HIO*I*H
r6 = k6*I2
r7 = k7*I2*HSO3
r8 = k8*SO3*H
r9 = k9*HSO3

# Mass Balance
dIO3 = -r1 + r3 - r4
dHSO3 = -r1 - r7 + r8 - r9
dHIO2 = r1 - r2 - r3 + r4
dI = -r2 + r3 - r4 - r5 + r6 - 2*r7
dH = -r2 + 2*r3 - 2*r4 - r5 + r6 + 3*r7 - r8 + r9
dHIO = 2*r2 - r3 + r4 - r5 + r6
dI2 = r5 - r6 - r7
dSO3 = -r8 + r9

# Integration time
tbegin = 0
tend = 480

# Scipy Integration
ode15s = scipy.integrate.ode()
