from main.models import *

# Create your models here.

class ArticleCategorie(BaseModel):
    nom_categorie=models.CharField(max_length=100,verbose_name='Title')
    slug=models.SlugField(max_length=200,verbose_name='Slug')

    class Meta:
        verbose_name="Categorie"

    def __str__(self) -> str:
        return self.nom_categorie
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.nom_categorie)
        
        super().save(*args,**kwargs)

class Article(BaseModel):
    titre=models.CharField(max_length=100,verbose_name='Titre')
    slug=models.SlugField(max_length=200,verbose_name='Slug')
    resume=models.CharField(max_length=200,blank=True,null=True,verbose_name="Resume")
    description=QuillField(blank=True,null=True,max_length=200,verbose_name='Description')
    image=models.ImageField(upload_to='articles_images',blank=True,null=True,name="image",verbose_name='Image')
    auteur=models.ForeignKey(CustomUser,on_delete=models.SET_NULL,blank=True,null=True,verbose_name='Auteur',
                            related_name='fk_user')
    categorie=models.ForeignKey(ArticleCategorie,on_delete=models.SET_NULL,null=True,blank=True,related_name='fk_categorie',
                                verbose_name='Categorie')
    statut=models.BooleanField(default=False,verbose_name="Statut")

    class Meta:
        ordering=['-created']
        verbose_name="Article"

    def __str__(self) -> str:
        return self.titre

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.titre)
        
        super().save(*args,**kwargs)
        
    def get_absolute_url(self):
        return reverse("mes_articles")
    
class Commentaire(BaseModel):
    article=models.ForeignKey(Article,on_delete=models.SET_NULL,null=True,blank=True,related_name='fk_blog_comment')
    content=models.TextField(blank=True,null=True,verbose_name='Commentaire')
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True,
                            related_name='fk_user_comment',
                            verbose_name='Auteur')
    
    class Meta:
        ordering=['-created']
        verbose_name="Commentaire"


