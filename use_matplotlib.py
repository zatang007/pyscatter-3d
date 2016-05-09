import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import axes3d
plt.rc('text', usetex=True)

def matplotlib_make_figure(figsize=(10,7), style='seaborn-dark'):
    try:
        plt.style.use(style)
    except IOError:
        plt.style.use('default')

    fig=plt.figure('scatter3d', figsize)
    plt.gcf().set_tight_layout(True)
    ax=fig.add_subplot(111,projection='3d')

    return fig, ax

def matplotlib_set_plot(ax, plot_title, outfile,
                        xaxis_label, yaxis_label, zaxis_label,
                        xaxis_range, yaxis_range, zaxis_range,
                        default_camera=(14,-120), 
                        hide_x=False, hide_y=False):
    tsize = 'medium'
    ax.set_xlabel(xaxis_label, fontsize=tsize)
    ax.set_ylabel(yaxis_label, fontsize=tsize)
    ax.set_zlabel(zaxis_label, fontsize=tsize)
    ax.ticklabel_format(axis='both', labelpad=150, useOffset=False)
    ax.set_xlim(*xaxis_range)
    ax.set_ylim(*yaxis_range)
    ax.set_zlim(*zaxis_range)
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
