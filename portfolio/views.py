from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Skill, Project, ContactMessage


def home(request):
    skills = Skill.objects.all()
    projects = Project.objects.all()

    return render(request, "portfolio/home.html", {
        "skills": skills,
        "projects": projects,
    })


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        send_mail(
            subject=f"New Portfolio Message - {name}",
            message=f"""
Name: {name}
Email: {email}

Message:
{message}
""",
            from_email=None,
            recipient_list=["eghorbani361@gmail.com"],
        )

        return redirect("contact")

    return render(request, "portfolio/contact.html")