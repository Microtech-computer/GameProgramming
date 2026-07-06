from django.http import HttpResponse
from django.contrib.auth.models import User


# ==========================
# CREATE USER
# ==========================
def create_user(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")

        if User.objects.filter(username=username).exists():
            return HttpResponse("Username already exists.")

        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )

        return HttpResponse(f"{user.username} created successfully.")

    return HttpResponse("Use POST request.")


# ==========================
# READ USERS
# ==========================
def user_report(request):

    users = User.objects.all()

    report = []

    report.append("=" * 120)
    report.append("{:^120}".format("USER REPORT"))
    report.append("=" * 120)

    report.append(
        f"{'S/N':<5}"
        f"{'ID':<6}"
        f"{'USERNAME':<20}"
        f"{'FIRST NAME':<20}"
        f"{'LAST NAME':<20}"
        f"{'EMAIL':<35}"
        f"{'ACTIVE'}"
    )

    report.append("-" * 120)

    for sn, user in enumerate(users, start=1):

        report.append(
            f"{sn:<5}"
            f"{user.id:<6}"
            f"{user.username:<20}"
            f"{user.first_name:<20}"
            f"{user.last_name:<20}"
            f"{user.email:<35}"
            f"{'YES' if user.is_active else 'NO'}"
        )

    report.append("-" * 120)
    report.append(f"Total Users : {users.count()}")

    return HttpResponse("<pre>" + "\n".join(report) + "</pre>")


# ==========================
# UPDATE USER
# ==========================
def update_user(request, user_id):

    if request.method == "POST":

        try:
            user = User.objects.get(id=user_id)

            user.username = request.POST.get("username", user.username)
            user.first_name = request.POST.get("first_name", user.first_name)
            user.last_name = request.POST.get("last_name", user.last_name)
            user.email = request.POST.get("email", user.email)

            password = request.POST.get("password")

            if password:
                user.set_password(password)

            user.save()

            return HttpResponse("User updated successfully.")

        except User.DoesNotExist:
            return HttpResponse("User not found.")

    return HttpResponse("Use POST request.")


# ==========================
# DELETE USER
# ==========================
def delete_user(request, user_id):

    if request.method == "POST":

        try:
            user = User.objects.get(id=user_id)

            username = user.username

            user.delete()

            return HttpResponse(f"{username} deleted successfully.")

        except User.DoesNotExist:
            return HttpResponse("User not found.")

    return HttpResponse("Use POST request.")