import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
def drawGraph(g1):
    g2 = np.asmatrix(g1)
    fig, axe = plt.subplots(figsize=(12,7))
    axe.set_title('Graf podany przez użytkownika')
    G = nx.from_numpy_matrix(g2, parallel_edges=False, create_using=nx.MultiGraph)
    layout = nx.spring_layout(G)
    nx.draw(G, layout, with_labels = True)
    edge = dict([((u,v),d['weight'])for u,v,d in G.edges(data=True)])
    nx.draw_networkx_edge_labels(G,ax=axe, pos=layout, edge_labels=edge)
    return plt.gcf()
def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure,canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top',fill='both',expand=1)
    return figure_canvas_agg
def delete_figure_agg(figure_agg):
    figure_agg.get_tk_widget().forget()
    plt.close('all')