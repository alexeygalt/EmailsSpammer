from django.views.generic import CreateView
from contact.forms import ContactForm
from contact.models import Contact
from .tasks import send_spam_mail


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = "/"
    template_name = "main/contact.html"

    def form_valid(self, form):
        form.save()
        # send(form.instance.email)
        send_spam_mail.delay(form.instance.email)
        return super().form_valid(form)
