from django.db import models

class DocumentCollection(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Document(models.Model):
    name = models.CharField(max_length=100)
    document_collection = models.ForeignKey(to=DocumentCollection, on_delete=models.CASCADE)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['name', 'document_collection'], name='unique_name_document_collection_constraints')]

    def __str__(self):
        return self.name

class Content(models.Model):
    name = models.CharField(max_length=100)
    file_filed_name = models.CharField(max_length=200, blank=True)
    tag_name = models.CharField(max_length=200)
    unit = models.CharField(max_length=100, blank=True)
    data_min_length = models.IntegerField(default=-1)
    data_max_length = models.IntegerField(default=-1)
    data_type = models.CharField(max_length=100)
    data_collection_device = models.CharField(max_length=100, blank=True)
    data_collection_period = models.CharField(max_length=100, blank=True)
    data_transper_period = models.CharField(max_length=100, blank=True)
    value = models.CharField(max_length=100, blank=True)
    original_value = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    etc = models.TextField(blank=True)
    document = models.ForeignKey(to=Document, on_delete=models.CASCADE)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['tag_name', 'document'], name='unique_tag_name_document_constraints')]

    def __str__(self):
        return self.name


