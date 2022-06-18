import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
def drawGraph(g1):
    g2 = np.asmatrix(g1)
    fig, axe = plt.subplots(figsize=(12,7))
    axe.set_title('Graf podany przez użytkownika')
    G = nx.from_numpy_matrix(g2, create_using=nx.MultiDiGraph())
    layout = nx.spring_layout(G)
    nx.draw(G, layout, with_labels = True)
    edge=dict([((u,v,),d['weight'])
             for u,v,d in G.edges(data=True)])
    nx.draw_networkx_edge_labels(G, pos=layout, edge_labels=edge, label_pos=0.3, font_size=7)
    return plt.gcf()
def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure,canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top',fill='both',expand=1)
    return figure_canvas_agg
def delete_figure_agg(figure_agg):
    figure_agg.get_tk_widget().forget()
    plt.close('all')