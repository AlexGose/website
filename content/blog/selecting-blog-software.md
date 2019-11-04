Date: 2019-11-04
Title: Starting a blog?  Consider Pelican, Docker, and Github Pages 
Tags: Pelican, Python, Docker, Github-Pages
Slug: selecting-blog-software
Summary: Why you might want to use a Docker container running Pelican to publish your website on Github Pages if you are starting a blog.

## Who should read this?

You want to start a blog, and you are no stranger to the command line or Linux operating system.  You do not expect to have a lot of traffic initially, but you are willing to make changes to your website over time.  You are not interested in making money off of your website at this time.  You view this project as an opportunity to learn more about aspects of web development that interest you.  

If this sounds like you, then read on.  In this post, I'll discuss why you might want to use [Pelican](https://blog.getpelican.com) running in a [Docker](https://www.docker.com) container to publish your blog on [Github Pages](https://pages.github.com/).  In a future post, I'll show you how to set up your own blog with these programs.

## Static Site Generators vs. WordPress

Most websites recommend a [Content Management System](https://en.wikipedia.org/wiki/Content_management_system) (CMS) for blogging, with [WordPress](https://wordpress.org) being the most popular suggestion.  Other options include [Joomla](https://www.joomla.org) and [Drupal](https://www.drupal.org).  

I have no experience using WordPress, but I think it is probably the best choice for most people getting started.  It doesn't require much, if any, knowledge of web development or programming, but knowing more will give you more options for your website.  Because WordPress is so popular, there are many resources and hosting options available.

WordPress is powerful and easy to use but does have some drawbacks.  The power comes from the ability to run programs on the web server.  This gives WordPress more capabilities than a [static website](https://en.wikipedia.org/wiki/Static_web_page), where a server simply sends files to website visitors.  This extra power requires more computing resources and administrative skill to ensure the smooth and safe operation of your website.  If you don't have these skills, then usually you end up paying someone who does.  This is often in the form of monthly fees paid to your hosting company.  

Static websites, like this one at the time this is being written, are a simpler option.  The relative ease of administering a static website often translates into a lower cost of hosting.  There are even a number of free options, which will be discussed below.  If you choose to be the administrator for the server of your site, then you will tend to have fewer operational and security concerns with a static website.  For this reason, a static blog is often an excellent first step towards building a more complex website. 

## Pelican 

[Pelican](https://blog.getpelican.com) is an open source static site generating software program written in python.  Other static site generating programs include [Hugo](https://gohugo.io) and [Jekyll](https://jekyllrb.com/).  

I don't have experience with other static site generating programs.  I mainly chose Pelican because it is written in python.  Since I know python, I can more easily view and modify the source code at some point in the future if I want.  Since Pelican is much simpler than a CMS program like WordPress, inspecting the source code should be easier too. 

I was also attracted to Pelican for its selection of [plugins](https://docs.getpelican.com/en/stable/plugins.html) and [themes](https://github.com/getpelican/pelican-themes), as well as the size of the development community.  I may experiment in the future and try other static site generating programs.

## Hosting 

I am currently using Github Pages for this website.  Github Pages allows you to use a custom domain, which can be purchased for a nominal yearly fee.  Although this hosting service is free, there are some [restrictions](https://help.github.com/en/github/working-with-github-pages/about-github-pages#guidelines-for-using-github-pages), which you should be aware of before using this service.  

Another free hosting option is [Gitlab Pages](https://about.gitlab.com/product/pages/), but I don't have experience with it.  If you decide to use a paid host, then a static website is usually easier or cheaper to run.  I may experiment with other hosting services in the future.

## Docker vs. Virtual Environments

With any static site generator, like Pelican, the content of your website is stored in a simple format, such as [markdown](https://en.wikipedia.org/wiki/Markdown) files.  The static site generator converts your content into fully formatted html files, which can be read and displayed by a browser.  These html files are sent from the web server to people visiting your website.

Like most python programs, Pelican can be installed in a virtual environment on your machine, such as your laptop computer.  This helps to isolate the program, which makes it easier to control dependencies and upgrades of the software.  However, it is still possible for two machines to have different virtual environments for the same project, and the process for setting up the environments on these machines can also be different. 

This can cause difficulties if more than one machine is used to build a website and the machines use different operating systems, or even different versions of the same operating system.  The complexity of maintaining environments on separate machines becomes more complex over time as software is upgraded.  Docker containers offer a solution to this problem by maintaining a consistent deployment of software across machines. 

Docker containers also provide a measure of isolation from other programs running on a single machine.  With Docker you can limit the risk of other programs modifying the directories or dependent libraries used by Pelican.  As you can see with the [docker file](https://github.com/AlexGose/website/blob/master/Dockerfile) used for this website, you can often maintain a relatively small amount of source code to build your website with Docker, avoiding the need to store files for plugins and themes directly on your machine.

## Conclusions  

In conclusion, there are many software and hosting options available for people getting started with building a blog website.  By seeing the options chosen for this website, and how they compare to some other popular options, I hope you will be in a better position to decide for yourself.  Keep in mind that there aren't really any bad choices.  Once you start, you can always make modifications or change the software, hosting, or content later.  Just be sure to backup your work.  If you don't mind the extra time and effort required, you might try more than one option now and pick the best later.  
