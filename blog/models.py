from django.db import models

# Create your models here.

from django.utils import timezone

hosp_no_choices = (("01", "Northwestern Medical Center"),("02", "North Country Hospital And Health Center"),("03", "Northeastern Vermont Regional Hospital"),("04", "Copley Hospital")
,("05", "University of Vermont Medical Center"),("06", "Central Vermont Hospital"),("08", "Rutland Regional Medical Center"),("09", "Porter Medical Center")
,("10", "Gifford Memorial Hospital"),("11", "Mount Ascutney Hospital And Health Center"),("12", "Springfield Hospital"),("14", "Grace Cottage Hospital")
,("15", "Brattleboro Memorial Hospital"),("16", "Southwestern Vermont Medical Center"),("17", "Fanny Allen Hospital"),("19", "Veterans Administration"))

atype_choices = (("01","Emergency"), ("02","Urgent"), ("03","Elective"), ("04","Newborn"),
                       ("05","Trauma"), ("06","Other / Missing"))

asource_choices = (("01","Other_Hosp"), ("02","Nurs_Facility"), ("03","Intermed_Care"), ("04","Another_Facility"),
                       ("05","Home_Own_Fam"), ("06","Home_Health"), ("07","Against_Medical"), ("08","Died"),
                       ("09","Home_Care"), ("10","Swing_Bed"),("11","Court"), ("12","Inpatient"), ("13","Still_Inpt"), ("00","Missing"))

age_grp_choices = (("01", "Under 1"), ("02", "1-17"), ("03", "18-24"), ("04", "25-29"), ("05", "30-34"), ("06", "35-39"), ("07", "40-44"), ("08", "45-49"),
("09", "50-54"), ("10", "55-59"), ("11", "60-64"), ("12", "65-69"), ("13", "70-74"), ("14", "75 and over"), ("15", "Unknown"))

aqtr_choices = (("1", "Jan-Mar"), ("2", "Apr-June"), ("3", "July-Sept"), ("4", "Oct-Dec"))
dqtr_choices = (("1", "Jan-Mar"), ("2", "Apr-June"), ("3", "July-Sept"), ("4", "Oct-Dec"))

class Post(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    hosp_no = models.CharField(max_length=15, choices = hosp_no_choices)
    atype = models.CharField(max_length=15, choices = atype_choices)
    asource = models.CharField(max_length=15, choices = asource_choices)
    age_grp = models.CharField(max_length=15, choices = age_grp_choices)
    sex = models.CharField(max_length=15, choices = (("1", "M"),("2","F")))
    drg = models.CharField(max_length=15)
    mdc = models.CharField(max_length=15)
    dx1 = models.CharField(max_length=15)
    px1 = models.CharField(max_length=15)
    dyear = models.CharField(max_length=15, choices = (("2000", "2000"), ("2001", "2001"), ("2002", "2002"), ("2003", "2003"), ("2004", "2004"),))
    aqtr = models.CharField(max_length=15, choices = aqtr_choices)
    dqtr = models.CharField(max_length=15, choices = dqtr_choices)
    CCSDX = models.CharField(max_length=15)
    pdays = models.CharField(max_length=15)
    dstat = models.CharField(max_length=15)

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.hosp_no
