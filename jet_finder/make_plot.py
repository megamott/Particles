import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from jet_finder import calculate_brightness


def make_2d_plot(cor_array, lum_array, folder=None):
    fig, ax = plt.subplots()

    ax.plot(cor_array, lum_array, color='b', linewidth=2)

    #  Scale intervals for Z axis
    ax.xaxis.set_major_locator(ticker.MultipleLocator(0.0025))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.00125))

    # For Luminance axis
    ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(20))

    # For SNR axis
    # ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
    # ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.05))

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

    plt.ylabel('Luminance')
    # plt.ylabel('SNR')
    plt.show()

    # calculate_brightness.save_pic('P_Z', fig, folder=folder)


if __name__ == '__main__':
    cor_arr, lum_arr = calculate_brightness.main(step=0.0005, max_range=0.0225, folder_name="7.17_IZ")
    make_2d_plot(cor_arr, lum_arr, "7.17_IZ")

    # cor_arr2, lum_arr2 = calculate_brightness.main(step=0.0025, max_range=0.0625, folder_name="2.5_IZ")
    # make_2d_plot(cor_arr2, lum_arr2, "2.5_IZ")
