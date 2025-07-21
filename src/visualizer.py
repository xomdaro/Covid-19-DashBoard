import plotly.express as px

def gerar_grafico(df, pais):
    df_pais = df[df['location'] == pais]
    fig = px.bar(
        df_pais,
        x='date',
        y='new_cases',
        labels={'date': 'Data', 'new_cases': 'Novos casos'},
        title=f"Novos casos diários de COVID-19 em {pais}",
        color_discrete_sequence=["royalblue"]
    )
    fig.update_layout(xaxis_title='Data', yaxis_title='Novos casos', template="plotly_white")
    return fig