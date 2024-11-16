import plotly.express as px
import pandas as pd

# example
data = {
    "time": ["2024-11-01 08:00", "2024-11-01 09:00", "2024-11-01 10:00", "2024-11-01 11:00"],
    "glucose_level": [120, 150, 130, 170]
}
df = pd.DataFrame(data)

fig = px.line(df, x="time", y="glucose_level", title="قند خون در طول زمان")
fig.update_layout(xaxis_title="زمان", yaxis_title="مقدار قند خون (mg/dL)")
fig.show()
