import logging
from django.utils import timezone
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.shortcuts import render, get_object_or_404
from blog.models import Post

logger = logging.getLogger(__name__)


# @cache_page(300)
# @vary_on_cookie
def index(request):
  posts = Post.objects.filter(published_at__lte=timezone.now())
  logger.debug("Got %d posts", len(posts))
  return render(request, "blog/index.html", {"posts": posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    logger.info(
      "Created comment on Post %d for user %s", post.pk, request.user
    )
    return render(request, "blog/post-detail.html", {"post": post})
