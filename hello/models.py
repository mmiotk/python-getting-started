from django.db import models

# Create your models here.

class Citations(models.Model):
    author = models.CharField(max_length=250)
    body = models.CharField(max_length=250)

    def __str__(self):
        return self.body + " " + self.author

class Lecturer(models.Model):
    SCIENTIFIC_TYPE_CHOICES = (('mgr', 'mgr'),
                               ('dr', 'dr'),
                               ('dr hab', 'dr hab.'),
                               ('prof', 'prof. dr hab.'),
                               ('dr hab UG', 'dr hab. prof. UG'),
                               ('dr hab PJATK', 'dr hab. prof. PJATK'))
    scientificType = models.CharField(max_length=20, choices=SCIENTIFIC_TYPE_CHOICES, default='dr')
    firstname = models.CharField(max_length=250)
    secondname = models.CharField(max_length=250)

    def __str__(self):
        return self.scientificType + " " + self.firstname + " " + self.secondname

class Lectures(models.Model):
    FACULTY_CHOICES = (('ug', 'UG'), ('pjatk', 'PJATK'))
    TYPE_STUDIES_CHOICES = (('stationary', 'Stationary'), ('extramural', 'Extramural'))
    YEAR_CHOICES = (('2020/2021', '2020/2021'), ('2019/2020', '2019/2020'))
    SEMESTER_CHOICES = (('winter', 'Winter'),('summer', 'Summer'))
    KIND_LECTURE_CHOICES = (('faculty', 'Faculty'), ('exercises', 'Exercises'), ('laboratory', 'Laboratory'))
    title = models.CharField(max_length=250)
    # lecturer = models.CharField(max_length=250)
    lecturer = models.ForeignKey(Lecturer, on_delete = models.CASCADE, related_name='lectures_lecturer')
    kind_lecture = models.CharField(max_length=20, choices=KIND_LECTURE_CHOICES, default='laboratory')
    year = models.CharField(max_length=20, choices=YEAR_CHOICES, default='2020/2021')
    semester = models.CharField(max_length=20, choices = SEMESTER_CHOICES, default='winter')
    typeOfStudies = models.CharField(max_length=20, choices=TYPE_STUDIES_CHOICES)
    faculty = models.CharField(max_length=20, choices=FACULTY_CHOICES)
    linkTeams = models.URLField()
    linkGrades = models.URLField()

class Presentations(models.Model):
    title = models.CharField(max_length=500)
    eventName = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    year = models.IntegerField()

    class Meta:
        ordering = ('-year',)

class ResearchPaper(models.Model):
    title = models.CharField(max_length=500)
    authors = models.ManyToManyField(Lecturer,related_name="papers_lecturers")
    submitted = models.BooleanField(default=False)
    inpress = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    journal = models.CharField(max_length=500, blank=True)
    volume = models.IntegerField(blank=True)
    number = models.IntegerField(blank=True)
    pages = models.CharField(max_length=100, blank=True)
    year = models.IntegerField(blank=True)
    doi = models.URLField(blank=True)
    url = models.URLField(blank=True)

    class Meta:
        ordering = ('-year',)