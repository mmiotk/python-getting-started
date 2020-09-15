import random
from hello.models import Citations

def get_random_citation(request):
    citations = Citations.objects.all()
    if(len(citations) > 0):
        randomIndex = random.randint(0, len(citations) - 1)
        randomCitation = citations[randomIndex]
    else:
        randomCitation = Citations(body="Cytat tygodnia", author="Jan Kowalski")
    return {
        'citationBody': randomCitation.body,
        'citationAuthor': randomCitation.author
    }