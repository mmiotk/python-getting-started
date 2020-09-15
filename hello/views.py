from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .helpers import get_sheet, get_faculty_login, is_vacation
from .models import  Lectures,  Presentations, ResearchPaper
# Create your views here.

def get_index_page(request):
    print(request.build_absolute_uri())
    print(request.get_host())
    print(request.get_raw_uri())
    print(request.get_full_path())
    print(request.is_secure())
    vacation = is_vacation()
    if request.user.is_authenticated and request.user.username != "admin":
        userFaculty = get_faculty_login(request.user)
    else:
        userFaculty = "bla"
    return render(request,'index.html', {'vacation': vacation, 'userFaculty': userFaculty})


def get_blog_page(request):
    return render(request, 'blog.html')

def get_logout_page(request):
    response = HttpResponseRedirect('/')
    for cookie in request.COOKIES:
        response.delete_cookie(cookie)
    return response


def get_teaching_page(request):
    domain = get_faculty_login(request.user)
    if (domain != None):
        if (domain == "ug"):
            lectures = Lectures.objects.filter(faculty="ug")
        elif (domain == "pjatk"):
            lectures = Lectures.objects.filter(faculty="pjatk")
        winterStationary = lectures.filter(semester='winter', typeOfStudies='stationary')
        winterExtramural = lectures.filter(semester='winter', typeOfStudies='extramural')
        summerStationary = lectures.filter(semester='summer', typeOfStudies='stationary')
        summerExtramural = lectures.filter(semester='summer', typeOfStudies='extramural')
    else:
        lectures = None
        winterStationary = None
        winterExtramural = None
        summerStationary = None
        summerExtramural = None
    return render(request, 'teaching.html', {'winterStationary': winterStationary,
                                                       'winterExtramural' : winterExtramural,
                                                       'summerStationary': summerStationary,
                                                       'summerExtramural': summerExtramural})

# def get_student_result(request):
#     user = request.user
#     r = get_sheet('https://inf.ug.edu.pl/~mmiotk/TestoweZajecia.xlsx', 'Obecnosci', user.username)
#     g = get_sheet('https://inf.ug.edu.pl/~mmiotk/TestoweZajecia.xlsx', 'Punkty', user.username)
#     return render(request, 'myWebsite/teaching.html', {'attendance_table': r, 'grades_table': g})

def get_student_result(request, filename):
    user = request.user
    domain = get_faculty_login(user)
    baseDir = ""
    if domain == 'ug':
        baseDir = 'https://inf.ug.edu.pl/~mmiotk/'+filename+".xlsx"
    elif domain == 'pjatk':
         baseDir = 'http://users.pja.edu.pl/~mmiotk/Grades/'+filename+".xlsx"
        # baseDir = 'https://pejot-my.sharepoint.com/:x:/g/personal/mmiotk_pjwstk_edu_pl/ER3AA20Wdu5Kl-2K1LqAf4MBt2IKjwRK-sjcbK77nxSCsg?e=1RPNfC'
    if domain != None:
        attendance = get_sheet(baseDir,'Obecnosci', user.username)
        grades = get_sheet(baseDir, 'Punkty', user.username)
        return render(request, 'grades.html', {'attendance': attendance, 'grades': grades})
    else:
        return render(request, 'grades.html')


def get_bibliography(request):
    return render(request, 'bibliography.html')

def get_research_page(request):
    inPressPublications = ResearchPaper.objects.filter(inpress=True)
    publishedPublications = ResearchPaper.objects.filter(published=True)
    submittedPublications = ResearchPaper.objects.filter(submitted=True)
    presentations = Presentations.objects.all()
    return render(request, 'research.html',
                  {
                      'publishedPublications' : publishedPublications,
                      'inPressPublications' : inPressPublications,
                      'submittedPublications': submittedPublications,
                      'presentations': presentations
                  })

# def handler404(request, exception):
#     context = {}
#     response = render(request, "errors/404.html", context=context)
#     response.status_code = 404
#     return response
#
#
# def handler500(request):
#     context = {}
#     response = render(request, "errors/500.html", context=context)
#     response.status_code = 500
#     print(response.content)
#     return response