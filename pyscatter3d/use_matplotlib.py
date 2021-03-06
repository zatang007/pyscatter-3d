import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import axes3d
plt.rc('text', usetex=True)
from logging import warning
import six

def matplotlib_make_figure(figsize=(10,7), style='seaborn-dark'):
    try:
        plt.style.use(style)
    except ValueError:
        warning(" matplotlib style %s not found." % style)
        pass

    fig=plt.figure('scatter3d', figsize)
    plt.gcf().set_tight_layout(True)
    ax=fig.add_subplot(111,projection='3d')

    return fig, ax

def matplotlib_set_plot(ax, plotter, outfile, default_camera=(14, -120),
                        hide_x=False, hide_y=False):
    ax.set_title(plotter.plot_title)

    tsize = 'medium'
    ax.set_xlabel(plotter.xaxis_label, fontsize=tsize)
    ax.set_ylabel(plotter.yaxis_label, fontsize=tsize)
    ax.set_zlabel(plotter.zaxis_label, fontsize=tsize)
    ax.ticklabel_format(axis='both', labelpad=150, useOffset=False)
    ax.set_xlim(*plotter.xaxis_range)
    ax.set_ylim(*plotter.yaxis_range)
    ax.set_zlim(*plotter.zaxis_range)
    ax.legend(fontsize='small')

    # getting a nice view over the whole mess in ppv
    ax.view_init(*default_camera)

    # hide axis-numbers:
    if hide_x:
        ax.get_xaxis().set_ticks([])
        ax.xaxis.set_visible(False)
        ax.get_xaxis().set_visible(False)
    if hide_y:
        ax.get_yaxis().set_ticks([])
        ax.yaxis.set_visible(False)
        ax.get_yaxis().set_visible(False)

    plt.draw()
    plt.savefig(outfile)
    plt.show()

def fix_axes3d_color(ax, col):
    """
    Setting color to None must cycle through the available colors
    as per matplotlib's philosophy. In some recent versions this was
    still not implemented however. This function fixes the issue.

    The issue was fixed in April 2016, and the code below hacks
    into: https://github.com/matplotlib/matplotlib/issues/5990
    """
    if col is not None:
        return col
    try:
        next_col = six.next(ax._get_patches_for_fill.prop_cycler)['color']
    except AttributeError:
        next_col = six.next(ax._get_patches_for_fill.color_cycle)
    return next_col
