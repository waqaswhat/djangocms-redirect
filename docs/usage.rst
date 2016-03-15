========
Usage
========

To write a redirect rule simply navigate to the django admin and
click on the redirects section.

Here you will be able to see the current redirect rules.

Click on th Add Redirect button on the top right.

You will need to fill just 4 fields:

* Site: select the site on which you want to add a redirect.
* Redirect from: The page that need to be redirect from: by clicking on the field you will be able to search for a django-cms page or you can write an url.
* Redirect to: The page to which you want the user to be redirected. You can select a page or provide an url.
* Response code: You can select 3 types of status_code header: 301 (a permanent redirection), 302 (a temporary redirection) or 410 (a permanent unavailable resource).

There are to ways of providing a 410 status code: you can either select it from the response code field or 
by simply leaving the redirect to field as blank.
