# 基于TensorFlow实现的CNN图片分类相关练习

标签（空格分隔）： 机器学习 TensorFlow CNN 深度学习

---

本项目主要参照《TensorFlow：实战Google深度学习框架》的6.5.2 TensorFlow实现迁移学习一节，目的在于熟悉TensorFlow框架以及CNN算法，采用迁移学习的方法减少了训练时间，提升了图片分类的准确度。具体包含以下几个模块：

**1.调用google的inception算法训练神经网络**
- *data_process.py*用于预处理数据，保存为numpy格式
- *fine_tuning.py*加载TensorFlow定义好的inception_v3框架完成训练。
需要下载[inception_v3.ckpt](http://download.tensorflow.org/models/inception_v3_2016_08_28.tar.gz)文件。实际在本人的笔记本上运行*data_process.py*程序时，会异常退出的情况，参考GitHub上的[issue](https://github.com/caicloud/tensorflow-tutorial/issues/96)说是内存不够，未得到解决

**2.迁移学习实现分类**
- *check_point.py*是《TensorFlow：实战Google深度学习框架》提供的完整图像分类程序，直接将google训练好的特征向量代替CNN卷积层的训练，只需完成全连接层的训练即可。迁移学习加快了训练的速度，模型的精准度可以达到90%。替换程序中的花种类识别为人体部位识别（图片数据爬取自keep社区），分为臀部、腿部、腹部、背部、胸部5个标签，精准度为80%左右。
- *download_by_tag.py*用于按类别爬取keep社区图片
- *download_image.py*用于爬取热门图片，图片连接地址存储与.txt文本中,具体可参见[keep爬虫项目](https://github.com/WinterYuan/keep_proj)

**3.基于CNN的鲜花种类分类**
- *CNN.py*为训练代码
- *CNN_test.py*为调用模型进行预测代码
以上两个程序转自[TensorFlow之CNN图像分类及模型保存与调用](http://blog.csdn.net/Enchanted_ZhouH/article/details/74116823),未采用迁移学习，识别准确率可以达到70%左右，数据集为公开数据集[flower_photos](http://download.tensorflow.org/example_images/flower_photos.tgz)

以上内容是近期学习了CNN相关知识的练习内容，参考书籍为《TensorFlow：实战Google深度学习框架》和吴恩达的[卷积神经网络课程](https://mooc.study.163.com/learn/2001281004?tid=2001392030#/learn/announce)






