from django.db import models
from django.core.mail import send_mail
from django.conf import settings


class ContactMessage(models.Model):
    """Model for storing contact form messages"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"

    def save(self, *args, **kwargs):
        """Send email notification when new message is created"""
        is_new = self.pk is None
        super().save(*args, **kwargs)
        
        if is_new:
            # Send email notification (optional - configure email settings)
            try:
                send_mail(
                    f'New Contact Message: {self.subject}',
                    f'Name: {self.name}\nEmail: {self.email}\n\nMessage:\n{self.message}',
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.ADMIN_EMAIL],
                    fail_silently=True,
                )
            except:
                pass  # Email sending failed but we don't want to break the form submission


class Product(models.Model):
    """Model for storing products"""
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('core:product_detail', kwargs={'pk': self.pk})
