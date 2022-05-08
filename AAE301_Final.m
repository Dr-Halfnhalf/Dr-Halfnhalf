clc
clear

g = 32.2;
p = 2.377 * (10^-3);
W = 2650;
S = 174;
j2 = 1346;
c = 4.9;
Clo = .307;
Cla = 4.41;
Clel = .43;
Cladot = 1.7;
Clq = 3.9;
x = 0;
Cmo = .04;
Cma = -.613;
Cmel = -1.122;
Cmadot = -7.27;
Cmq = -12.4;
n = .7;
eps = 0;
et = 0;
Cdm = .0223;
k = .0554;
Cldm = 0;
th = 100;
el = .0278;

tiledlayout(3,2);
output = sim('AAE301_FinalSimu');

nexttile
plot(output.alpha);
title('Time History of Angle of Attack')
xlabel('Time (sec)')
ylabel('Angle of Attack (degrees)')

nexttile
plot(output.gamma)
title('Time History of Flight Path Angle')
xlabel('Time (sec)')
ylabel('Flight Path Angle (degrees)')

 nexttile
 plot(output.velocity)
 title('Time History of Speed of Aircraft')
 xlabel('Time (sec)')
 ylabel('Velocity (ft/sec)')

nexttile
plot(output.Altitude)
title('Time History of Altitude')
xlabel('Time (sec)')
ylabel('Altitude (ft)')

alt = output.Altitude.Data;
ran = output.HorizRange.Data;

nexttile
plot(ran,alt)
title('Aircraft Trajectory')
xlabel('Horizontal Range (ft)')
ylabel('Altitude (ft)')
xlim([0,max(ran)])
