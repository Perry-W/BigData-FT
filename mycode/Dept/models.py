import datetime

from django.db import models
from django.utils import timezone
# Create your models here.
# from django.db import models


class FtTest(models.Model):
    test_date=models.DateField()
    test_business = models.CharField(max_length=200)
    test_product = models.CharField(max_length=200)
    test_pac = models.CharField(max_length=200)
    test_person = models.CharField(max_length=200)
    test_site = models.CharField(max_length=200)

    

    class Meta:         # 注意，是模型的子类，要缩进！
        verbose_name="场测任务"
        verbose_name_plural = "FT测试表"
    #pub_date = models.DateTimeField('date published')s

    def __str__(self):
        return str(self.pk)+"_"+self.test_person+"_"+self.test_product+"_"+str(self.test_date)

    #def __str__(self):
     #   return self

"""
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
"""
    


class CALL(models.Model):
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    """
    call_operator=models.CharField(max_length=200)
    #call_terminal = models.CharField(max_length=200) #DUT/REF
    #call_business_direction_ter = models.CharField(max_length=200)#MO/MT veideo_MO_DUT/viedeo_MT_REF
    #call_videodirection = models.CharField(max_length=200)#MO/MT
    call_environment = models.CharField(max_length=200)#强/弱/动态
    voicecall_mo_dut_vonr = models.FloatField(max_length=200,null=True,blank=True)
    voicecall_mo_ref_vonr = models.FloatField(max_length=200,null=True,blank=True)
    voicecall_mt_dut_vonr = models.FloatField(max_length=200,null=True,blank=True)
    voicecall_mt_ref_vonr = models.FloatField(max_length=200,null=True,blank=True)

    voicecall_mo_dut_epsfb = models.FloatField(max_length=200,null=True,blank=True)
    voicecall_mo_ref_epsfb = models.FloatField(max_length=200,null=True,blank=True)
    voicecall_mt_dut_epsfb = models.FloatField(max_length=200,null=True,blank=True)
    voicecall_mt_ref_epsfb = models.FloatField(max_length=200,null=True,blank=True)

    voicecall_mo_dut_volte = models.FloatField(max_length=200,null=True,blank=True)
    voicecall_mo_ref_volte = models.FloatField(max_length=200,null=True,blank=True)
    voicecall_mt_dut_volte = models.FloatField(max_length=200,null=True,blank=True)
    voicecall_mt_ref_volte = models.FloatField(max_length=200,null=True,blank=True)

    voicecall_mo_dut_csfb = models.FloatField(max_length=200,null=True,blank=True)
    voicecall_mo_ref_csfb = models.FloatField(max_length=200,null=True,blank=True)
    voicecall_mt_dut_csfb = models.FloatField(max_length=200,null=True,blank=True)
    voicecall_mt_ref_csfb = models.FloatField(max_length=200,null=True,blank=True)
    #call_epsfb = models.FloatField(max_length=200,null=True,blank=True)#呼通业务暂时做常测试的几种
    #call_volte = models.FloatField(max_length=200,null=True,blank=True)
    #call_csfb = models.FloatField(max_length=200,null=True,blank=True)
    fttest=models.ForeignKey(FtTest,on_delete=models.CASCADE)

    class Meta:         # 注意，是模型的子类，要缩进！
        verbose_name="通话业务"
        verbose_name_plural = "FT通话业务"

    def __str__(self):
        return "CALL"+"_"+str(self.pk)+"_"+self.call_operator+"_"+str(self.fttest)


class SS(models.Model):
    call_operator=models.CharField(max_length=200)

    dut_cf=models.FloatField(max_length=200,null=True,blank=True)
    dut_cb=models.FloatField(max_length=200,null=True,blank=True)
    dut_cw=models.FloatField(max_length=200,null=True,blank=True)

    ref_cf=models.FloatField(max_length=200,null=True,blank=True)
    ref_cb=models.FloatField(max_length=200,null=True,blank=True)
    ref_cw=models.FloatField(max_length=200,null=True,blank=True)

    fttest=models.ForeignKey(FtTest,on_delete=models.CASCADE)
    
    class Meta:         # 注意，是模型的子类，要缩进！
        verbose_name="补充业务"
        verbose_name_plural = "FT补充业务"

    def __str__(self):
        return "SS"+"_"+str(self.pk)+"_"+self.call_operator+"_"+str(self.fttest)
    
class TTFF(models.Model):
    test_person=models.CharField(max_length=200)
    test_date=models.DateField()
    test_product=models.CharField(max_length=200)
    test_hdware=models.CharField(max_length=200)
    test_branch=models.CharField(max_length=200)
    test_pac=models.CharField(max_length=200)
    test_state=models.CharField(max_length=200)
    test_location=models.CharField(max_length=200)#测试地点
    setup_pattern=models.CharField(max_length=200)#启动模式
    search_pattern=models.CharField(max_length=200)#搜星模式

    dut1_ttff_ave=models.FloatField(max_length=200,null=True,blank=True)
    dut1_ttff_cep68=models.FloatField(max_length=200,null=True,blank=True)
    dut1_ttff_cep95=models.FloatField(max_length=200,null=True,blank=True)
    dut1_ttff_max=models.FloatField(max_length=200,null=True,blank=True)
    dut1_acc_ave=models.FloatField(max_length=200,null=True,blank=True)
    dut1_acc_cep68=models.FloatField(max_length=200,null=True,blank=True)
    dut1_acc_cep95=models.FloatField(max_length=200,null=True,blank=True)
    dut1_acc_max=models.FloatField(max_length=200,null=True,blank=True)

    dut2_ttff_ave=models.FloatField(max_length=200,null=True,blank=True)
    dut2_ttff_cep68=models.FloatField(max_length=200,null=True,blank=True)
    dut2_ttff_cep95=models.FloatField(max_length=200,null=True,blank=True)
    dut2_ttff_max=models.FloatField(max_length=200,null=True,blank=True)
    dut2_acc_ave=models.FloatField(max_length=200,null=True,blank=True)
    dut2_acc_cep68=models.FloatField(max_length=200,null=True,blank=True)
    dut2_acc_cep95=models.FloatField(max_length=200,null=True,blank=True)
    dut2_acc_max=models.FloatField(max_length=200,null=True,blank=True)

    ref_ttff_ave=models.FloatField(max_length=200,null=True,blank=True)
    ref_ttff_cep68=models.FloatField(max_length=200,null=True,blank=True)
    ref_ttff_cep95=models.FloatField(max_length=200,null=True,blank=True)
    ref_ttff_max=models.FloatField(max_length=200,null=True,blank=True)
    ref_acc_ave=models.FloatField(max_length=200,null=True,blank=True)
    ref_acc_cep68=models.FloatField(max_length=200,null=True,blank=True)
    ref_acc_cep95=models.FloatField(max_length=200,null=True,blank=True)
    ref_acc_max=models.FloatField(max_length=200,null=True,blank=True)

    stdvalues=models.FloatField(max_length=200,null=True,blank=True)#标准值

    result=models.BooleanField()

    class Meta:         # 注意，是模型的子类，要缩进！
        verbose_name="TTFF"
        verbose_name_plural = "GNSS业务表"

    def __str__(self):
        return "TTFF"+"_"+str(self.pk)+"_"+self.test_person+"_"+str(self.test_date)

"""
class Meta:
        ordering = ["-c_time"]
        verbose_name = "FT"
        verbose_name_plural = "FT"
"""

    

