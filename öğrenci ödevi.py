""" tht pyhton ödevi 
*******************gamze1i-wamp!r*******************
"""
class Exam():
	score = 0 
	def __init__(self,dogrusoru_sayisi, yanlissoru_sayisi):
		self.dogrusoru_sayisi = dogrusoru_sayisi
		self.yanlissoru_sayisi = yanlissoru_sayisi          
		
		toplam = self.dogrusoru_sayisi + self.yanlissoru_sayisi
		puan = 100 / toplam 

		self.score = self.dogrusoru_sayisi * puan


	def __float__(self):
		return self.score


class Student():
	ogrenci_kadi = A
	not_listesi = []
	avg_score = 0
	def __init__(self,ogrenci_kadi):
		self.ogrenci_kadi = ogrenci_kadi

	def add_exam(self,sinav_notu):
		self.sinav_notu = int(float(sinav_notu))
		self.not_listesi.append(self.sinav_notu)
		
		self.avg_score += self.sinav_notu
		adet = len(self.not_listesi)
		self.avg_score = self.avg_score / adet

	def __float__(self):
		return float(self.avg_score)

class Class():
	not_listesi = []
	class_avg = 0

	def add_student(self,ogrenci_not):
		self.ogrenci_not = int(float(ogrenci_not))
		self.not_listesi.append(self.ogrenci_not)

		self.class_avg += self.ogrenci_not
		adet = len(self.not_listesi)
		self.class_avg = self.class_avg / adet



