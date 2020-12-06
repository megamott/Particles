import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from jetFinder import calculate_brightness


# cor_arr, lum_arr = calculate_brightness.main()

def make_2d_plot(cor_array, lum_array):
    fig, ax = plt.subplots()

    ax.plot(cor_array, lum_array, color='b', linewidth=2)

    #  Scale intervals
    ax.xaxis.set_major_locator(ticker.MultipleLocator(0.0025))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.00125))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))

    #  Add lines of general grid
    ax.grid(which='major', color='k')

    #  Turn on grid
    ax.minorticks_on()

    #  Grid view
    ax.grid(which='minor',
            color='gray',
            linestyle=':')

    fig.set_figwidth(18)
    fig.set_figheight(14)

    plt.xlabel('Z coordinate')
    plt.ylabel('SNR')
    plt.show()

    calculate_brightness.save_pic('P3_Z_SNR', fig)


# if __name__ == '__main__':
#     make_2d_plot(cor_arr, lum_arr)
