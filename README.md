# celestial-observer

Mapping the degrees of rotation and Mars-Sun angle from the horizon_results.txt file.

Soon, these results will be used to rotate 3D printed models mounted on spur gears and a stepper motor to simulate the rotation of Mars and the angle of the Sun.

## Example Usage

### Python Command

The python command below will generate a CSV file with the degrees of rotation and Mars-Sun angle from the horizon_results.txt file.

```bash
python3 generate_degrees.py --data horizon_results.txt --output generated.csv
```

### generated.csv example

```csv
Timestamp,Rotation (Degrees),Mars-Sun Angle (Degrees)
2024-11-17 00:00,0.0,4.433
2024-11-18 00:00,350.89,4.433
2024-11-19 00:00,341.78,4.424
2024-11-20 00:00,332.68,4.417
2024-11-21 00:00,323.57,4.413
2024-11-22 00:00,314.46,4.422
2024-11-23 00:00,305.35,4.432
2024-11-24 00:00,296.24,4.444
2024-11-25 00:00,287.14,4.457
2024-11-26 00:00,278.03,4.463
2024-11-27 00:00,268.92,4.474
2024-11-28 00:00,259.81,4.483
2024-11-29 00:00,250.7,4.486
2024-11-30 00:00,241.6,4.493
2024-12-01 00:00,232.49,4.505
2024-12-02 00:00,223.38,4.513
2024-12-03 00:00,214.27,4.504
2024-12-04 00:00,205.16,4.5
2024-12-05 00:00,196.06,4.489
2024-12-06 00:00,186.95,4.482
2024-12-07 00:00,177.84,4.477
2024-12-08 00:00,168.73,4.49
2024-12-09 00:00,159.62,4.495
2024-12-10 00:00,150.52,4.479
2024-12-11 00:00,141.41,4.469
2024-12-12 00:00,132.3,4.475
2024-12-13 00:00,123.19,4.482
2024-12-14 00:00,114.08,4.463
2024-12-15 00:00,104.98,4.442
2024-12-16 00:00,95.87,4.436
2024-12-17 00:00,86.76,4.417
```

### horizon_results.txt example

```txt
*******************************************************************************
 Revised: June 21, 2016                 Mars                            499 / 4
 
 PHYSICAL DATA (updated 2019-Oct-29):
  Vol. mean radius (km) = 3389.92+-0.04   Density (g/cm^3)      =  3.933(5+-4)
  Mass x10^23 (kg)      =    6.4171       Flattening, f         =  1/169.779
  Volume (x10^10 km^3)  =   16.318        Equatorial radius (km)=  3396.19
  Sidereal rot. period  =   24.622962 hr  Sid. rot. rate, rad/s =  0.0000708822 
  Mean solar day (sol)  =   88775.24415 s Polar gravity m/s^2   =  3.758
  Core radius (km)      = ~1700           Equ. gravity  m/s^2   =  3.71
  Geometric Albedo      =    0.150                                              

  GM (km^3/s^2)         = 42828.375214    Mass ratio (Sun/Mars) = 3098703.59
  GM 1-sigma (km^3/s^2) = +- 0.00028      Mass of atmosphere, kg= ~ 2.5 x 10^16
  Mean temperature (K)  =  210            Atmos. pressure (bar) =    0.0056 
  Obliquity to orbit    =   25.19 deg     Max. angular diam.    =  17.9"
  Mean sidereal orb per =    1.88081578 y Visual mag. V(1,0)    =  -1.52
  Mean sidereal orb per =  686.98 d       Orbital speed,  km/s  =  24.13
  Hill's sphere rad. Rp =  319.8          Escape speed, km/s    =   5.027
                                 Perihelion  Aphelion    Mean
  Solar Constant (W/m^2)         717         493         589
  Maximum Planetary IR (W/m^2)   470         315         390
  Minimum Planetary IR (W/m^2)    30          30          30
*******************************************************************************


*******************************************************************************
Ephemeris / WWW_USER Sat Nov 16 21:00:57 2024 Pasadena, USA      / Horizons    
*******************************************************************************
Target body name: Mars (499)                      {source: mar097}
Center body name: Earth (399)                     {source: DE441}
Center-site name: GEOCENTRIC
*******************************************************************************
Start time      : A.D. 2024-Nov-17 00:00:00.0000 UT      
Stop  time      : A.D. 2024-Dec-17 00:00:00.0000 UT      
Step-size       : 1440 minutes
*******************************************************************************
Target pole/equ : IAU_MARS                        {West-longitude positive}
Target radii    : 3396.19, 3396.19, 3376.2 km     {Equator_a, b, pole_c}       
Center geodetic : 0.0, 0.0, -6378.137             {E-lon(deg),Lat(deg),Alt(km)}
Center cylindric: 0.0, 0.0, 0.0                   {E-lon(deg),Dxy(km),Dz(km)}
Center pole/equ : ITRF93                          {East-longitude positive}
Center radii    : 6378.137, 6378.137, 6356.752 km {Equator_a, b, pole_c}       
Target primary  : Sun
Vis. interferer : MOON (R_eq= 1737.400) km        {source: DE441}
Rel. light bend : Sun                             {source: DE441}
Rel. lght bnd GM: 1.3271E+11 km^3/s^2                                          
Atmos refraction: NO (AIRLESS)
RA format       : HMS
Time format     : CAL 
Calendar mode   : Mixed Julian/Gregorian
EOP file        : eop.241115.p250211                                           
EOP coverage    : DATA-BASED 1962-JAN-20 TO 2024-NOV-15. PREDICTS-> 2025-FEB-10
Units conversion: 1 au= 149597870.700 km, c= 299792.458 km/s, 1 day= 86400.0 s 
Table cut-offs 1: Elevation (-90.0deg=NO ),Airmass (>38.000=NO), Daylight (NO )
Table cut-offs 2: Solar elongation (  0.0,180.0=NO ),Local Hour Angle( 0.0=NO )
Table cut-offs 3: RA/DEC angular rate (     0.0=NO )                           
******************************************************************************************************************************************************************************
 Date__(UT)__HR:MN     R.A._____(ICRF)_____DEC    APmag   S-brt             delta      deldot     S-O-T /r     S-T-O  Sky_motion  Sky_mot_PA  RelVel-ANG  Lun_Sky_Brt  sky_SNR
******************************************************************************************************************************************************************************
$$SOE
 2024-Nov-17 00:00     08 24 37.39 +21 18 52.4   -0.275   4.433  0.90232828303216 -12.3776532  111.4001 /L   36.0868   0.5899180   94.177810   -62.53249         n.a.     n.a.
 2024-Nov-18 00:00     08 25 36.82 +21 17 56.5   -0.294   4.433  0.89519370130305 -12.3294581  112.1788 /L   35.8198   0.5662262   93.754762   -63.57453         n.a.     n.a.
 2024-Nov-19 00:00     08 26 33.83 +21 17 09.2   -0.322   4.424  0.88808802246582 -12.2775003  112.9677 /L   35.5439   0.5420519   93.273886   -64.64080         n.a.     n.a.
 2024-Nov-20 00:00     08 27 28.34 +21 16 30.8   -0.349   4.417  0.88101350803572 -12.2214743  113.7671 /L   35.2587   0.5173951   92.725783   -65.73147         n.a.     n.a.
 2024-Nov-21 00:00     08 28 20.31 +21 16 01.6   -0.371   4.413  0.87397259226996 -12.1610899  114.5770 /L   34.9641   0.4922634   92.098973   -66.84645         n.a.     n.a.
 2024-Nov-22 00:00     08 29 09.68 +21 15 41.9   -0.382   4.422  0.86696787004419 -12.0960820  115.3979 /L   34.6599   0.4666712   91.379250   -67.98551         n.a.     n.a.
 2024-Nov-23 00:00     08 29 56.42 +21 15 32.1   -0.392   4.432  0.86000208192078 -12.0262106  116.2297 /L   34.3458   0.4406397   90.548759   -69.14818         n.a.     n.a.
 2024-Nov-24 00:00     08 30 40.45 +21 15 32.5   -0.399   4.444  0.85307810056241 -11.9512572  117.0729 /L   34.0216   0.4141971   89.584722   -70.33379         n.a.     n.a.
 2024-Nov-25 00:00     08 31 21.73 +21 15 43.4   -0.406   4.457  0.84619892031024 -11.8710180  117.9275 /L   33.6871   0.3873805   88.457630   -71.54133         n.a.     n.a.
 2024-Nov-26 00:00     08 32 00.21 +21 16 05.0   -0.419   4.463  0.83936765002187 -11.7852995  118.7938 /L   33.3421   0.3602388   87.128624   -72.76926         n.a.     n.a.
 2024-Nov-27 00:00     08 32 35.84 +21 16 37.6   -0.427   4.474  0.83258750828365 -11.6939149  119.6719 /L   32.9864   0.3328378   85.545652   -74.01534         n.a.     n.a.
 2024-Nov-28 00:00     08 33 08.56 +21 17 21.5   -0.438   4.483  0.82586181967981 -11.5966841  120.5620 /L   32.6197   0.3052670   83.637685   -75.27618         n.a.     n.a.
 2024-Nov-29 00:00     08 33 38.32 +21 18 16.9   -0.454   4.486  0.81919401070731 -11.4934348  121.4644 /L   32.2419   0.2776516   81.305911   -76.54672         n.a.     n.a.
 2024-Nov-30 00:00     08 34 05.09 +21 19 24.1   -0.468   4.493  0.81258760405207 -11.3840070  122.3792 /L   31.8527   0.2501704   78.410154   -77.81924         n.a.     n.a.
 2024-Dec-01 00:00     08 34 28.80 +21 20 43.2   -0.475   4.505  0.80604621026054 -11.2682573  123.3065 /L   31.4520   0.2230866   74.748050   -79.08182         n.a.     n.a.
 2024-Dec-02 00:00     08 34 49.42 +21 22 14.4   -0.487   4.513  0.79957351634298 -11.1460651  124.2465 /L   31.0397   0.1967992   70.024363   -80.31562         n.a.     n.a.
 2024-Dec-03 00:00     08 35 06.89 +21 23 58.0   -0.515   4.504  0.79317327147513 -11.0173364  125.1993 /L   30.6154   0.1719314   63.811882   -81.49036         n.a.     n.a.
 2024-Dec-04 00:00     08 35 21.19 +21 25 53.9   -0.539   4.500  0.78684927059101 -10.8820069  126.1651 /L   30.1791   0.1494724   55.526197   -82.55672         n.a.     n.a.
 2024-Dec-05 00:00     08 35 32.26 +21 28 02.4   -0.569   4.489  0.78060533710329 -10.7400423  127.1439 /L   29.7307   0.1309635   44.507078   -83.43639         n.a.     n.a.
 2024-Dec-06 00:00     08 35 40.08 +21 30 23.5   -0.596   4.482  0.77444530613078 -10.5914360  128.1358 /L   29.2699   0.1185686   30.430892   -84.01732         n.a.     n.a.
 2024-Dec-07 00:00     08 35 44.60 +21 32 57.2   -0.621   4.477  0.76837300948507 -10.4362051  129.1411 /L   28.7968   0.1145681   14.144903   -84.17808         n.a.     n.a.
 2024-Dec-08 00:00     08 35 45.80 +21 35 43.6   -0.627   4.490  0.76239226346710 -10.2743852  130.1596 /L   28.3111   0.1200359   357.92677   -83.85482         n.a.     n.a.
 2024-Dec-09 00:00     08 35 43.64 +21 38 42.7   -0.642   4.495  0.75650686051674 -10.1060219  131.1915 /L   27.8127   0.1339966   343.99635   -83.08676         n.a.     n.a.
 2024-Dec-10 00:00     08 35 38.10 +21 41 54.4   -0.676   4.479  0.75072056609115  -9.9311609  132.2369 /L   27.3017   0.1542952   333.11090   -81.97497         n.a.     n.a.
 2024-Dec-11 00:00     08 35 29.15 +21 45 18.6   -0.705   4.469  0.74503712267067  -9.7498334  133.2957 /L   26.7779   0.1788867   324.90680   -80.61747         n.a.     n.a.
 2024-Dec-12 00:00     08 35 16.77 +21 48 55.3   -0.718   4.475  0.73946026296690  -9.5620391  134.3682 /L   26.2413   0.2063166   318.72189   -79.08395         n.a.     n.a.
 2024-Dec-13 00:00     08 35 00.93 +21 52 44.3   -0.729   4.482  0.73399373346813  -9.3677280  135.4542 /L   25.6917   0.2356516   313.98118   -77.41846         n.a.     n.a.
 2024-Dec-14 00:00     08 34 41.61 +21 56 45.5   -0.767   4.463  0.72864132693207  -9.1667887  136.5538 /L   25.1293   0.2663017   310.26707   -75.64789         n.a.     n.a.
 2024-Dec-15 00:00     08 34 18.79 +22 00 58.7   -0.806   4.442  0.72340691887572  -8.9590471  137.6671 /L   24.5538   0.2978827   307.29178   -73.78869         n.a.     n.a.
 2024-Dec-16 00:00     08 33 52.44 +22 05 23.8   -0.830   4.436  0.71829450032235  -8.7442806  138.7940 /L   23.9654   0.3301292   304.85835   -71.85117         n.a.     n.a.
 2024-Dec-17 00:00     08 33 22.57 +22 10 00.4   -0.866   4.417  0.71330819907812  -8.5222430  139.9346 /L   23.3640   0.3628429   302.83047   -69.84204         n.a.     n.a.
$$EOE
******************************************************************************************************************************************************************************
Column meaning:
 
TIME

  Times PRIOR to 1962 are UT1, a mean-solar time closely related to the
prior but now-deprecated GMT. Times AFTER 1962 are in UTC, the current
civil or "wall-clock" time-scale. UTC is kept within 0.9 seconds of UT1
using integer leap-seconds for 1972 and later years.

  Conversion from the internal Barycentric Dynamical Time (TDB) of solar
system dynamics to the non-uniform civil UT time-scale requested for output
has not been determined for UTC times after the next July or January 1st.
Therefore, the last known leap-second is used as a constant over future
intervals.

  Time tags refer to the UT time-scale conversion from TDB on Earth
regardless of observer location within the solar system, although clock
rates may differ due to the local gravity field and no analog to "UT"
may be defined for that location.

  Any 'b' symbol in the 1st-column denotes a B.C. date. First-column blank
(" ") denotes an A.D. date.
 
CALENDAR SYSTEM

  Mixed calendar mode was active such that calendar dates after AD 1582-Oct-15
(if any) are in the modern Gregorian system. Dates prior to 1582-Oct-5 (if any)
are in the Julian calendar system, which is automatically extended for dates
prior to its adoption on 45-Jan-1 BC.  The Julian calendar is useful for
matching historical dates. The Gregorian calendar more accurately corresponds
to the Earth's orbital motion and seasons. A "Gregorian-only" calendar mode is
available if such physical events are the primary interest.

  NOTE: "n.a." in output means quantity "not available" at the print-time.
 
 'R.A._____(ICRF)_____DEC' =
  Astrometric right ascension and declination of the target center with
respect to the observing site (coordinate origin) in the reference frame of
the planetary ephemeris (ICRF). Compensated for down-leg light-time delay
aberration.

  Units: RA  in hours-minutes-seconds of time,    HH MM SS.ff{ffff}
         DEC in degrees-minutes-seconds of arc,  sDD MN SC.f{ffff}
 
 'APmag   S-brt' =
  The targets' approximate apparent visual magnitude and surface brightness.
For planets and natural satellites, output is restricted to solar phase angles
covered by observational data. Outside the observed phase angle range, "n.a."
may be output to avoid extrapolation beyond the limit of model validity.

   For Earth-based observers, the estimated dimming due to atmospheric
absorption (extinction) is available as a separate, requestable quantity.

   Surface brightness is the average airless visual magnitude of a
square-arcsecond of the illuminated portion of the apparent disk. It is
computed only if the target radius is known.

   Units: MAGNITUDES & MAGNITUDES PER SQUARE ARCSECOND
 
 'delta      deldot' =
   Apparent range ("delta", light-time aberrated) and range-rate ("delta-dot")
of the target center relative to the observer. A positive "deldot" means the
target center is moving away from the observer, negative indicates movement
toward the observer.  Units: AU and KM/S
 
 'S-O-T /r' =
   Sun-Observer-Target apparent SOLAR ELONGATION ANGLE seen from the observers'
location at print-time.

   The '/r' column provides a code indicating the targets' apparent position
relative to the Sun in the observers' sky, as described below:

   Case A: For an observing location on the surface of a rotating body, that
body rotational sense is considered:

    /T indicates target TRAILS Sun   (evening sky: rises and sets AFTER Sun)
    /L indicates target LEADS Sun    (morning sky: rises and sets BEFORE Sun)

   Case B: For an observing point that does not have a rotational model (such
as a spacecraft), the "leading" and "trailing" condition is defined by the
observers' heliocentric ORBITAL motion:

    * If continuing in the observers' current direction of heliocentric
       motion would encounter the targets' apparent longitude first, followed
       by the Sun's, the target LEADS the Sun as seen by the observer.

    * If the Sun's apparent longitude would be encountered first, followed
       by the targets', the target TRAILS the Sun.

   Two other codes can be output:
    /* indicates observer is Sun-centered    (undefined)
    /? Target is aligned with Sun center     (no lead or trail)

   The S-O-T solar elongation angle is numerically the minimum separation
angle of the Sun and target in the sky in any direction. It does NOT indicate
the amount of separation in the leading or trailing directions, which would
be defined along the equator of a spherical coordinate system.

   Units: DEGREES
 
 'S-T-O' =
   The Sun-Target-Observer angle; the interior vertex angle at target center
formed by a vector from the target to the apparent center of the Sun (at
reflection time on the target) and the apparent vector from target to the
observer at print-time. Slightly different from true PHASE ANGLE (requestable
separately) at the few arcsecond level in that it includes stellar aberration
on the down-leg from target to observer.  Units: DEGREES
 
 'Sky_motion  Sky_mot_PA  RelVel-ANG' =
  Total apparent angular rate of the target in the plane-of-sky. "Sky_mot_PA"
is the position angle of the target's direction of motion in the plane-of-sky,
measured counter-clockwise from the apparent of-date north pole direction.
"RelVel-ANG" is the flight path angle of the target's relative motion with
respect to the observer's line-of-sight, in the range [-90,+90], where positive
values indicate motion away from the observer, negative values are toward the
observer:

  -90 = target is moving directly toward the observer
    0 = target is moving at right angles to the observer's line-of-sight
  +90 = target is moving directly away from the observer

UNITS:  ARCSECONDS/MINUTE, DEGREES, DEGREES
 
 'Lun_Sky_Brt  sky_SNR' =
  Sky brightness due to moonlight scattered by Earth's atmosphere at the
target's position in the sky. "sky_SNR" is the visual signal-to-noise ratio
(SNR) of the target's surface brightness relative to background sky. Output
only for topocentric Earth observers when both the Moon and target are above
the local horizon and the Sun is in astronomical twilight (or further) below
the horizon, and the target is not the Moon or Sun. If all conditions are
not met, "n.a." is output. Galactic brightness, local sky light-pollution
and weather are NOT considered. Lunar opposition surge is considered. The
value returned is accurate under ideal conditions at the approximately 8-23%
level, so is a useful but not definitive value.

  If the target-body radius is also known, "sky_SNR" is output. This is the
approximate visual signal-to-noise ratio of the target's brightness divided
by lunar sky brightness. When sky_SNR < 1, the target is dimmer than the
ideal moonlight-scattering background sky, so unlikely to be detectable at
visual wavelengths. In practice, visibility requires sky_SNR > 1 and a
detector sensitive enough to reach the target's magnitude, even if it isn't
washed out by moonlight. When relating magnitudes and brightness values,
keep in mind their logarithmic relationship m2-m1 = -2.5*log_10(b2/b1).

  UNITS: VISUAL MAGNITUDES / ARCSECOND^2, and unitless ratio

Computations by ...

    Solar System Dynamics Group, Horizons On-Line Ephemeris System
    4800 Oak Grove Drive, Jet Propulsion Laboratory
    Pasadena, CA  91109   USA

    General site: https://ssd.jpl.nasa.gov/
    Mailing list: https://ssd.jpl.nasa.gov/email_list.html
    System news : https://ssd.jpl.nasa.gov/horizons/news.html
    User Guide  : https://ssd.jpl.nasa.gov/horizons/manual.html
    Connect     : browser        https://ssd.jpl.nasa.gov/horizons/app.html#/x
                  API            https://ssd-api.jpl.nasa.gov/doc/horizons.html
                  command-line   telnet ssd.jpl.nasa.gov 6775
                  e-mail/batch   https://ssd.jpl.nasa.gov/ftp/ssd/hrzn_batch.txt
                  scripts        https://ssd.jpl.nasa.gov/ftp/ssd/SCRIPTS
    Author      : Jon.D.Giorgini@jpl.nasa.gov

******************************************************************************************************************************************************************************

```
