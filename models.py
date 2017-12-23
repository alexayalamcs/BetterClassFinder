from django.db import models

class CourseDate(models.Model):
    time_start = models.CharField(max_length=8)
    time_end = models.CharField(max_length=8)
    time_start_period = models.CharField(max_length=4)
    time_end_period = models.CharField(max_length=4)
    time_days = models.CharField(max_length=8)
    time_building = models.CharField(max_length=8)
    time_room_number = models.CharField(max_length=8)

# Create your models here.
class Course(models.Model):
    course_subject = models.CharField(max_length=8)
    course_number = models.CharField(max_length=8)
    course_name = models.CharField(max_length=128)
    course_prof_name = models.CharField(max_length=128)
    course_gur = models.CharField(max_length=32)
    course_credits = models.CharField(max_length=8)
    course_fee = models.CharField(max_length=32, blank=True)
    course_restrictions = models.CharField(max_length=512, blank=True)
    course_prereq = models.CharField(max_length=512, blank=True)
    course_additional_info = models.CharField(max_length=512, blank=True)
    course_crn = models.CharField(max_length=8)

    primary_course_date = models.OneToOneField(
        CourseDate,
        on_delete=models.CASCADE,
        related_name='primary_course_date',
    )
    
    secondary_course_date = models.OneToOneField(
        CourseDate,
        on_delete=models.CASCADE,
        related_name='secondary_course_date',
        null=True,
    )
    
    '''
    def getPrimaryDate(self):
        return self.course_dates.all()[0]
    
    def getSecondaryDate(self):
        size = len(self.course_dates.all())
        
        return None if size == 1 else self.course_dates.all()[1]
    
    def getDates(self):
        dateModels = self.course_dates.all()
        amountOfDates = len(dateModels)
        
        if (amountOfDates == 0):
            return ''
        elif(amountOfDates == 1):
            return dateModels[0].time_days
        
        dateString = ''
        dateList = ['M', 'T', 'W', 'R', 'F', 'S', 'U']
        
        for x in range(7):
            char = dateList[x]
            
            for date in dateModels:
                if (char in date.time_days):
                    dateString += char
                    break
            
        return dateString
    '''

class Term(models.Model):
    name = models.CharField(max_length=16)
    courses = models.ManyToManyField(Course)
