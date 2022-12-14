import pygal
from die import Die
# 创建一个骰子
die = Die()
# 掷骰子
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, die.numsize+1):
    frequency = results.count(value)
    frequencies.append(frequency)
# 结果可视化
hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
# hist.render_in_browser()
print(frequencies)
