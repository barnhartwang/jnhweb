from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name ="home.html"
    def get_context_data(self,*args, **kwargs):
        context = super(HomePageView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/JHFHeader.jpg'
        return context

class Choir2024View(TemplateView):
    template_name="choir2024.html"
    def get_context_data(self,*args, **kwargs):
        context = super(Choir2024View, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/jhfchoirHeader.jpg'
        return context

class InMyLifetimeView(TemplateView):
    template_name="inmylifetime.html"
    def get_context_data(self,*args, **kwargs):
        context = super(InMyLifetimeView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/choirheader.jpg'
        return context

class JHFChoirView(TemplateView):
    template_name = "jhfchoir.html"
    def get_context_data(self,*args, **kwargs):
        context = super(JHFChoirView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/jhfchoirHeader.jpg'
        return context

class JHFCharityConcertsView(TemplateView):
    template_name = "jhfcharityconcerts.html"
    def get_context_data(self,*args, **kwargs):
        context = super(JHFCharityConcertsView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/jhfcharityconcertsheader.jpg'
        return context


class JHFCharityConcerts2018View(TemplateView):
    template_name="jhfcharityconcerts2018.html"
    def get_context_data(self,*args, **kwargs):
        context = super(JHFCharityConcerts2018View, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/jhfcharityconcertsheader.jpg'
        return context

class ForThoseWhoLove(TemplateView):
    template_name="forthosewholove.html"
    def get_context_data(self,*args, **kwargs):
        context = super(ForThoseWhoLove, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/jhfchoirHeader.jpg'
        return context

### Chinese New Year #### 
class ChineseNewYear2023View(TemplateView):
    template_name="chinesenewyear2023.html"
    def get_context_data(self,*args, **kwargs):
        context = super(ChineseNewYear2023View, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/ChineseNewYear2023Header.jpg'
        return context

class ChineseNewYear2024View(TemplateView):
    template_name="chinesenewyear2024.html"
    def get_context_data(self,*args, **kwargs):
        context = super(ChineseNewYear2024View, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/ChineseNewYear2024Header.jpg'
        return context

class ChineseNewYearView(TemplateView):
    template_name="chinesenewyear.html"
    def get_context_data(self,*args, **kwargs):
        context = super(ChineseNewYearView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/ChineseNewYearHeader.jpg'
        return context

#### Health ####
class MedicineSeriesView(TemplateView):
    template_name = "medicineseries.html"
    def get_context_data(self,*args, **kwargs):
        context = super(MedicineSeriesView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/medicineseriesHeader.jpg'
        return context


class HealthTalksView(TemplateView):
    template_name = "healthtalk.html"
    def get_context_data(self,*args, **kwargs):
        context = super(HealthTalksView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/healthtalkheader.jpg'
        return context
    

class BeautyCareView(TemplateView):
    template_name = "beautycare.html"
    def get_context_data(self,*args, **kwargs):
        context = super(BeautyCareView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/beautycareheader.jpg'
        return context


class PhysicalCareAndRehabitationView(TemplateView):
    template_name = "physicalcareandrehabitation.html"

class NewHealthIdeasView(TemplateView):
    template_name = "newhealthideas.html"

class PhysicalConditioningView(TemplateView):
    template_name="physicalconditioning.html"
    def get_context_data(self,*args, **kwargs):
        context = super(PhysicalConditioningView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/medicineseriesHeader.jpg'
        return context
    

class PhysicalConditioningAView(TemplateView):
    template_name="physicalconditioninga.html"
    def get_context_data(self,*args, **kwargs):
        context = super(PhysicalConditioningAView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/medicineseriesHeader.jpg'
        return context

class CosmetologyView(TemplateView):
    template_name="Cosmetology.html"
    def get_context_data(self,*args, **kwargs):
        context = super(CosmetologyView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/medicineseriesHeader.jpg'
        return context

class MoxibustionView(TemplateView):
    template_name="Moxibustion.html"
    def get_context_data(self,*args, **kwargs):
        context = super(MoxibustionView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/medicineseriesHeader.jpg'
        return context

class WetView(TemplateView):
    template_name="wet.html"
    def get_context_data(self,*args, **kwargs):
        context = super(WetView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/medicineseriesHeader.jpg'
        return context

class ColdView(TemplateView):
    template_name="cold.html"
    def get_context_data(self,*args, **kwargs):
        context = super(ColdView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/medicineseriesHeader.jpg'
        return context

class HayFeverView(TemplateView):
    template_name="hayfever.html"
    def get_context_data(self,*args, **kwargs):
        context = super(HayFeverView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/medicineseriesHeader.jpg'
        return context

class ScarView(TemplateView):
    template_name="scar.html"
    def get_context_data(self,*args, **kwargs):
        context = super(ScarView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/medicineseriesHeader.jpg'
        return context

class AlzheimerView(TemplateView):
    template_name="Alzheimer.html"
    def get_context_data(self,*args, **kwargs):
        context = super(AlzheimerView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/medicineseriesHeader.jpg'
        return context

class BadTemperView(TemplateView):
    template_name="badtemper.html"
    def get_context_data(self,*args, **kwargs):
        context = super(BadTemperView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/medicineseriesHeader.jpg'
        return context

class LoseWeightView(TemplateView):
    template_name="loseweight.html"
    def get_context_data(self,*args, **kwargs):
        context = super(LoseWeightView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/medicineseriesHeader.jpg'
        return context

class HyperthermiaView(TemplateView):
    template_name="hyperthermia.html"
    def get_context_data(self,*args, **kwargs):
        context = super(HyperthermiaView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/medicineseriesHeader.jpg'
        return context

class DeficiencyView(TemplateView):
    template_name="deficiency.html"
    def get_context_data(self,*args, **kwargs):
        context = super(DeficiencyView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/medicineseriesHeader.jpg'
        return context

class SleepView(TemplateView):
    template_name="sleep.html"
    def get_context_data(self,*args, **kwargs):
        context = super(SleepView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/medicineseriesHeader.jpg'
        return context

class ImmuneSystemView(TemplateView):
    template_name="immunesystem.html" 
    def get_context_data(self,*args, **kwargs):
        context = super(ImmuneSystemView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/medicineseriesHeader.jpg'
        return context

class GuaShaTherapyView(TemplateView):
    template_name="guashatherapy.html"
    def get_context_data(self,*args, **kwargs):
        context = super(GuaShaTherapyView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/medicineseriesHeader.jpg'
        return context

class FastingView(TemplateView):
    template_name="fasting.html"
    def get_context_data(self,*args, **kwargs):
        context = super(FastingView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/medicineseriesHeader.jpg'
        return context

class Covid19View(TemplateView):
    template_name="covid19.html"
    def get_context_data(self,*args, **kwargs):
        context = super(Covid19View, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/medicineseriesHeader.jpg'
        return context

class befriendwithyourbody1View(TemplateView):
    template_name="befriendwithyourbody1.html"
    def get_context_data(self,*args, **kwargs):
        context = super(befriendwithyourbody1View, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/medicineseriesHeader.jpg'
        return context

class TakeCareOfYourHeartView(TemplateView):
    template_name="TakeCareOfYourHeart.html"
    def get_context_data(self,*args, **kwargs):
        context = super(TakeCareOfYourHeartView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/medicineseriesHeader.jpg'
        return context

class ChineseMedicineDietTherapyView(TemplateView):
    template_name="ChineseMedicineDietTherapy.html"
    def get_context_data(self,*args, **kwargs):
        context = super(ChineseMedicineDietTherapyView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/medicineseriesHeader.jpg'
        LowBackPain
        return context
    
class LowBackPainView(TemplateView):
    template_name="LowBackPain.html"
    def get_context_data(self,*args, **kwargs):
        context = super(LowBackPainView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/medicineseriesHeader.jpg'        
        return context

class ConstipateView(TemplateView):
    template_name="constipate.html"

class HealthPorridgeView(TemplateView):
    template_name="healthporridge.html"
    def get_context_data(self,*args, **kwargs):
        context = super(HealthPorridgeView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/healthtalkheader.jpg'
        return context

class NourishYourHeartView(TemplateView):
    template_name="NourishYourHeart.html"
    def get_context_data(self,*args, **kwargs):
        context = super(NourishYourHeartView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/healthtalkheader.jpg'
        return context

class ChineseFoodTherapeuticsView(TemplateView):
    template_name="ChineseFoodTherapeutics.html"
    def get_context_data(self,*args, **kwargs):
        context = super(ChineseFoodTherapeuticsView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/healthtalkheader.jpg'
        return context

class ReduceWeightView(TemplateView):
    template_name="ReduceWeight.html"
    def get_context_data(self,*args, **kwargs):
        context = super(ReduceWeightView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/beautycareheader.jpg'
        return context

class RinsingRicesForYourBeautyView(TemplateView):
    template_name="RinsingRicesForYourBeauty.html"
    def get_context_data(self,*args, **kwargs):
        context = super(RinsingRicesForYourBeautyView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/beautycareheader.jpg'
        return context

class ColumnbyLingyaoWuView(TemplateView):
    template_name="ColumnbyLingyaoWu.html"
    def get_context_data(self,*args, **kwargs):
        context = super(ColumnbyLingyaoWuView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/ColumnbyLingyaoWuheader.jpg'
        return context

class ConfusionaboutTimeView(TemplateView):
    template_name="ConfusionaboutTime.html"
    def get_context_data(self,*args, **kwargs):
        context = super(ConfusionaboutTimeView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/ColumnbyLingyaoWuheader.jpg'
        return context

class WeWillBeOlderTomorrowView(TemplateView):
    template_name="WeWillBeOlderTomorrow.html"
    def get_context_data(self,*args, **kwargs):
        context = super(WeWillBeOlderTomorrowView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/ColumnbyLingyaoWuheader.jpg'
        return context

class AddMoreHumortoYourLifeView(TemplateView):
    template_name="AddMoreHumortoYourLife.html"
    def get_context_data(self,*args, **kwargs):
        context = super(AddMoreHumortoYourLifeView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/ColumnbyLingyaoWuheader.jpg'
        return context

 ## Culture Talk ###       
class JHFCultureTalksView(TemplateView):
    template_name="JHFCultureTalks.html"
    def get_context_data(self,*args, **kwargs):
        context = super(JHFCultureTalksView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/culturetalkheader.jpg'
        return context

class ShadowPlayView(TemplateView):
    template_name="ShadowPlay.html"
    def get_context_data(self,*args, **kwargs):
        context = super(ShadowPlayView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/culturetalkheader.jpg'
        return context

class EstatePlanningView(TemplateView):
    template_name="EstatePlanning.html"
    def get_context_data(self,*args, **kwargs):
        context = super(EstatePlanningView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/culturetalkheader.jpg'
        return context

class HappyLivingHomeView(TemplateView):
    template_name="HappyLivingHome.html"
    def get_context_data(self,*args, **kwargs):
        context = super(HappyLivingHomeView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/culturetalkheader.jpg'
        return context

class TeaCultureView(TemplateView):
    template_name='TeaCulture.html'
    def get_context_data(self,*args, **kwargs):
        context = super(TeaCultureView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/culturetalkheader.jpg'
        return context
        
class GetCloserView(TemplateView):
    template_name="GetCloser.html"
    def get_context_data(self,*args, **kwargs):
        context = super(GetCloserView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/culturetalkheader.jpg'
        return context

class JHFActivitiesView(TemplateView):
    template_name="JHFActivities.html"
    def get_context_data(self,*args, **kwargs):
        context = super(JHFActivitiesView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/jhfactivitiesHeader.jpg'
        return context

class RealEstateView(TemplateView):
    template_name="RealEstate.html"
    def get_context_data(self,*args, **kwargs):
        context = super(RealEstateView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/jhfactivitiesHeader.jpg'
        return context

class InvestinahouseView(TemplateView):
    template_name="Investinahouse.html"
    def get_context_data(self,*args, **kwargs):
        context = super(InvestinahouseView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/jhfactivitiesHeader.jpg'
        return context

class RespecttheElderlyDinnerView(TemplateView):
    template_name="RespecttheElderlyDinner.html"
    def get_context_data(self,*args, **kwargs):
        context = super(RespecttheElderlyDinnerView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/jhfactivitiesHeader.jpg'
        return context


class CulturearoundtheWorldView(TemplateView):
    template_name="CulturearoundtheWorld.html"
    def get_context_data(self,*args, **kwargs):
        context = super(CulturearoundtheWorldView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/CulturearoundtheWorldheader.jpg'
        return context

class DieAtTheAgeOfView(TemplateView):
    template_name="DieAtTheAgeOf.html"
    def get_context_data(self,*args, **kwargs):
        context = super(DieAtTheAgeOfView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/CulturearoundtheWorldheader.jpg'
        return context
    
class TheHiddenMeaningsofYinYangView(TemplateView):
    template_name="TheHiddenMeaningsofYinYang.html"
    def get_context_data(self,*args, **kwargs):
        context = super(TheHiddenMeaningsofYinYangView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/CulturearoundtheWorldheader.jpg'
        return context

class ShaoKongchuanBelCantoView(TemplateView):
    template_name="ShaoKongchuanBelCanto.html"
    def get_context_data(self,*args, **kwargs):
        context = super(ShaoKongchuanBelCantoView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/ShaoKongchuanBelCantoHader.jpg'
        return context

class SuiHaopingView(TemplateView):
    template_name="suihaoping.html"

class SuiHaopingToastmastersView(TemplateView):
    template_name="suihaopingtoastmasters.html"
    def get_context_data(self,*args, **kwargs):
        context = super(SuiHaopingToastmastersView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/suihaopingtoastmastersHader.jpg'
        return context

class SuiHaopingconcertView(TemplateView):
    template_name = "suihaopingconcert.html"
    def get_context_data(self,*args, **kwargs):
        context = super(SuiHaopingconcertView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/suihaopingconcertHeader.jpg'
        return context

class MissionsView(TemplateView):
    template_name = "Missions.html"
    def get_context_data(self,*args, **kwargs):
        context = super(MissionsView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/MissionsHeader.jpg'
        return context

class ContactUsView(TemplateView):
    template_name = "ContactUs.html"
    def get_context_data(self,*args, **kwargs):
        context = super(ContactUsView, self).get_context_data(*args,**kwargs)
        context['headerimage'] = '/static/images/ContactUsHeader.jpg'
        return context
        