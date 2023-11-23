import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def create_currency_plot(currency, frequency):
    
    dff = pd.read_csv('data\\final_merged.csv')
    dff['Date'] = pd.to_datetime(dff['Date'], format='%d-%b-%y')
    dff.set_index('Date', inplace=True)

    if frequency == 'Weekly':
        df_resampled = dff.resample('W').mean()
    elif frequency == 'Monthly':
        df_resampled = dff.resample('M').mean()
    elif frequency == 'Quarterly':
        df_resampled = dff.resample('Q').mean()
    elif frequency == 'Yearly':
        df_resampled = dff.resample('Y').mean()    
    else:
        raise ValueError("Invalid frequency. Supported frequencies are 'weekly', 'monthly', and 'quarterly'.")

    highest_idx = df_resampled[currency].idxmax()
    lowest_idx = df_resampled[currency].idxmin()
    
    fig = px.line(df_resampled, x=df_resampled.index, y=df_resampled[currency],
                  title=f'{frequency.capitalize()} Exchange Rates for {currency}',
                  line_shape='linear')
    
    
    # Add a Scatter trace for missing values
    missing_values_trace = go.Scatter(x=df_resampled.index[df_resampled[currency].isnull()],
                                      #y=df_resampled[currency][df_resampled[currency].isnull()],
                                      mode='markers',
                                      marker=dict(color='black', size=5),
                                      showlegend=False,
                                     )
    fig.add_trace(missing_values_trace)
    fig.add_trace(go.Scatter(x=[highest_idx], y=[df_resampled[currency].loc[highest_idx]],
                             mode='markers',
                             marker=dict(color='green', size=10, symbol='triangle-up'),
                             name='Highest Value'))
    
    fig.add_trace(go.Scatter(x=[lowest_idx], y=[df_resampled[currency].loc[lowest_idx]],
                             mode='markers',
                             marker=dict(color='red', size=10, symbol='triangle-down'),
                             name='Lowest Value'))
    
    #Show the graph
    graph_html = fig.to_html(full_html=False)
    return graph_html