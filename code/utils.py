
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('fivethirtyeight')

def plot_asset_allocation(tickers, weights_list, method_name):
    """
    This visualisation code provides an intuitive understanding of the distribution of weights 
    across various stocks in the portfolio according to the chosen allocation strategy.
    """

    # Assume you have your weights in a dictionary
    fig = go.Figure(data=[go.Pie(labels=tickers, 
                                values=weights_list, 
                                hole=.5)])  # To create a donut chart, we use 'hole' argument

    fig.update_layout(
        title_text=f"Asset allocation via {method_name}", 
        # Add annotations in the center of the donut pie
        annotations=[dict(text='Portfolio', x=0.5, y=0.5, font_size=20, showarrow=False)]
    )

    fig.show()

def viz_stocks(df, title, xtitle, ytitle):
    fig = go.Figure()

    # Add traces for each stock
    for column in df.columns:
        fig.add_trace(go.Scatter(x=df.index, y=df[column], mode='lines', name=column))

    # Add a title and labels
    fig.update_layout(title=title,
                    xaxis=dict(title=xtitle),
                    yaxis=dict(title=ytitle))

    # Display the plot
    fig.show()


def viz_cov_matrix(matrix, title):

    plt.figure(figsize=(10, 6)) # You can adjust the size of your plot

    # Creating the heatmap
    sns.heatmap(matrix, annot=False, cmap='coolwarm', fmt='.2f', linewidths=2)

    plt.title(title)
    plt.show()