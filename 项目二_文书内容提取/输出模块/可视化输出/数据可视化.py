# -*-  coding: utf-8 -*-
# Author: cao wang
# Datetime : 2020
# software: PyCharm
# 收获:x、y轴均可以多，但是需要对应数量,分词即为类型，类型可以不用写入，但是必须要有，如同散点图一样
import pandas as pd
import plotly.express as px
import plotly.offline as py


path = "J:\PyCharm项目\项目\项目二_文书内容提取\输出模块\可视化输出\\规约完成文件\\test汇总表(去重）.xlsx"
data_frame = pd.read_excel(path,index_col=None)
print(type(data_frame))
print(data_frame)

fig =px.bar(data_frame, x="频率",y='分词', animation_frame="文书名",color='文书名',orientation ='h',
            range_x=[0,data_frame.频率.max()],range_y=[0,data_frame.分词.max()],animation_group="分词"


           )




'''
x,y为标签
hover_name="country":交互元素标签
range_x，range_y为轴坐标的刻度
animation_group="country"为坐标观测点，若为continent就会变小
'''

fig.show()
#当词一致的时候就会叠加

'''保存'''
py.plot(fig)



