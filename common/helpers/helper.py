from django.shortcuts import redirect

def permissions(user_role):
    if user_role == "student":
        return redirect('studenthome')
    elif user_role == "staff":
        return redirect('staffhome')
    elif user_role == "editor":
        return redirect('editorhome')
    elif user_role == "admin":
        return redirect('adminhome')
    else:
        return redirect('logout')