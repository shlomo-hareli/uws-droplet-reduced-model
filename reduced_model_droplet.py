"""
UWS Droplet Reduced Model (Tabulated Framework)

This implementation provides:
- Bilinear interpolation in (T, r) space
- Progress-variable-based reduced trajectory reconstruction
- Validation against detailed tabulated chemistry

Author: Shlomo Hareli
KIT - Institute of Technical Thermodynamics
"""
import numpy as np
import matplotlib.pyplot as plt
######################################################################################################################
#UWS droplet reduced model tabulation                                                                                #
#Extended table layout:                                   
#     0-phi       1-dphi_dt    2-d2eq       3-md          4-temp          5-rho          6-w_h2o       7-w_ur_s 
#     8-w_ur_l    9-w_hnco     10-w_biu_l   11-w_biu_s    12-w_triu       13-w_cya_s     14-w_amd_s    15-e_h20 
#     16-e_nh3    17-e_cya     18-e_amd     19-e_ur       20-e_hnco       21-qdot        22-t          23-mdot  
################################################################################################################

T_GRID=np.array([400.0,410.0,420.0,430.0,440.0,450.0,460.0,470.0,480.0,490.0,500.0,510.0,520.0,530.0,540.0,550.0,560.0,570.0,580.0,590.0,600.0,610.0,620.0,630.0,640.0,650.0])
R_GRID=np.array([2.5e-06, 7.5e-06, 1.25e-05, 1.75e-05, 2.25e-05, 2.75e-05, 3.25e-05, 3.75e-05, 4.25e-05, 4.75e-05, 5.25e-05, 5.75e-05, 6.25e-05, 6.75e-05, 7.25e-05, 7.75e-05, 8.25e-05, 8.75e-05, 9.25e-05, 9.75e-05, 1.02e-04, 1.05e-04])


# Bilinear_interpolation 
# input: table, T_grid, R_grid and the intgration points T0 and r0
# output: 2D arrayof the properties
def bilinear_interpolation(table, T_grid, r_grid, T0, r0):
    """
    Bilinear interpolation in temperature-radius space.

    Parameters
    ----------
    table : ndarray
        Lookup table.
    T_grid : ndarray
        Temperature grid [K].
    R_grid : ndarray
        Radius grid [m].
    T0 : float
        Query temperature [K].
    r0 : float
        Query radius [m].

    Returns
    -------
    ndarray
        Interpolated trajectory.
    """

    # 1a) --------------- Temperature indices ----------------
    iT1 = np.searchsorted(T_grid, T0)
    iT0 = max(iT1 - 1, 0)
    iT1 = min(iT1, len(T_grid) - 1)

    # 1b)--------------- Radius indices ---------------------
    iR1 = np.searchsorted(r_grid, r0)
    iR0 = max(iR1 - 1, 0)
    iR1 = min(iR1, len(r_grid) - 1)

    # 2)--------------- Compute weights ---------------------
    T0v, T1v = T_grid[iT0], T_grid[iT1]
    R0v, R1v = r_grid[iR0], r_grid[iR1]
    
    t = 0 if T1v == T0v else (T0 - T0v) / (T1v - T0v)
    u = 0 if R1v == R0v else (r0 - R0v) / (R1v - R0v)
    
    # 3)--------------- 4 Corner slices (always valid) --------
    Q11 = table[:, :, iT0, iR0]
    Q12 = table[:, :, iT0, iR1]
    Q21 = table[:, :, iT1, iR0]
    Q22 = table[:, :, iT1, iR1]

    # --------------- Bilinear (becomes linear if dim=1) ---
    return ((1-t)*(1-u)*Q11 + (1-t)*u*Q12+t*(1-u)*Q21 + t*u*Q22)

    #I=Bilinear_interpolation_TR(table, T_grid, r_grid, T0, r0)


# Reduced model data
# Input: interpolated_data,n_points
# Output: reduced_model_data
def generate_reduced_model_data(interpolated_data, n_points=10000):
    """
    Generate reduced trajectory using the progress variable.

    Parameters
    ----------
    interpolated_data : ndarray
        Interpolated trajectory.
    n_points : int
        Number of integration points.

    Returns
    -------
    ndarray
        Reduced trajectory.
    """

    time = np.linspace(0.0, 10.0, n_points)
    reduced = np.zeros((n_points, 24))
    dt = time[1] - time[0]
    phi = interpolated_data[-1, 0]

    for i in range(n_points):
        dphi_dt = np.interp(phi,interpolated_data[:, 0],interpolated_data[:, 1])
        reduced[i, 0] = phi
        reduced[i, -1] = dphi_dt

        for j in range(22):
            reduced[i, j + 2] = np.interp(phi,interpolated_data[:, 0],interpolated_data[:, j + 2])
        phi += dt * dphi_dt

    return reduced

# Example comparison between interpolated and reduced trajectories.
# p denotes the property index in the extended table.
# Default: p = 12 (triuret mass fraction).
def plot_triuret(interpolated_data, reduced_data,p=12):
    """
    Example: Compare detailed and reduced triuret evolution.
    """

    plt.figure()

    plt.plot(
        interpolated_data[:, 22],
        interpolated_data[:, p],
        "r*",
        label="Interpolated"
    )

    plt.plot(
        reduced_data[:, 22],
        reduced_data[:, p],
        "g--",
        label="Reduced"
    )

    plt.xlabel("Time [s]")
    plt.ylabel("Triuret mass fraction [-]")
    plt.legend()
    plt.tight_layout()
    plt.show()



def main():

    table = np.load("uws_droplet_table.npy") # load table
    temperature = 523.0 # temperatue parameter
    radius = 3.5e-5 # radius parameter

    interpolated = bilinear_interpolation(table, T_GRID, R_GRID, temperature, radius)

    reduced = generate_reduced_model_data(interpolated, n_points=10000)

    plot_triuret(interpolated, reduced)


if __name__ == "__main__":
    main()







