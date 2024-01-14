from bokeh.plotting import figure, output_file, show

x = [1,2,3,4,5]
y = [5,3,4,9,7]

output_file('index,html')

#plotes

p = figure(
    title='Grafico'
    x_axis_label='Eixo X'
    y_axis_label='Eixo Y'
)

#Render glyph
p.line(x,y, legend='Test', line_with=2)

show(p)