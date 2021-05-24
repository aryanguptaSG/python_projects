from django.test import SimpleTestCase
from django.urls import resolve ,reverse
from TheatreAPI.views import occupy,vacate ,get_info

class TestUrls(SimpleTestCase):
	def test_occupy_url_is_resolves(self):
		url = reverse('occupy')
		self.assertEquals(resolve(url).func,occupy)

	def test_vacate_url_is_resolves(self):
		url = reverse('vacate',args = [2])
		self.assertEquals(resolve(url).func,vacate)

	def test_get_info_url_is_resolves(self):
		url = reverse('get_info',args = [2])
		self.assertEquals(resolve(url).func,get_info)