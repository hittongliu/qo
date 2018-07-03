class data:

    def _init_(self):
        field_type = dict() # 字符型特征的所有特征值，数字型特征只保留key，value为空
        distinct_valueset = dict() # 数字型特征的所有特征值
        instances = dict() # 所有的样本
        filed_name = tuple() # 所有的特征名称和label标签

    def _init_ (self, fileName):
        """初始化类"""
        for line in open(fileName):
            if line == '\n':
                continue
            fields = line.split(',')
