class exam ():
	"""sınav sınıfı oluşturduk.."""
	def __init__(self,dogru_sayisi ="bilgi yok" ,yanlis_sayisi = "bilgi yok" ):
		"""burada sınav puanını hesaplamak için toplam soru sayısı bölü 100 yapıp soru başı puanı hesaplıyacaz."""
		self.dogru_sayisi = dogru_sayisi
		self.yanlis_sayisi = yanlis_sayisi
		toplam_soru = self.dogru_sayisi + self.yanlis_sayisi
		Exam.score = 100 / toplam_soru
	def __float__(self):
		return float(exam.score)

class student(exam):
	ogrenci_adi = []
	not_listesi = []
	avg_score = 0
	def __init__(self,ogrenci_adi = "bilgi yok" ):
		self.ogrenci_adi = ogrenci_adi

	def add_exam(self,sinav_notu = "0"):
		self.sinav_notu = int(float(sinav_notu))
		self.not_listesi.append(self.sinav_notu)
		
		self.avg_score += self.sinav_notu
		toplam = len(self.not_listesi)
		self.avg_score = self.avg_score / toplam

	def __float__(self):
		return float(self.avg_score)


class Class(Student):

not_listesi = []
	class_avg = 0

	def add_student(self,ogrenci_not ="0"):
		self.ogrenci_not = int(float(ogrenci_not))
		self.not_listesi.append(self.ogrenci_not)

		self.class_avg += self.ogr_not
		toplam = len(self.not_listesi)
		self.class_avg = self.class_avg / toplam

		