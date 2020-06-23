import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <title>Mini Project</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel = "icon" type = "image/png" href = "images/Logo.png">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
    <style type="text/css">
        body {
            animation-name: example;
            animation-duration: 4s;
        }
        ul > li > a:hover {
            display:block;
            background-color:lightblue;
            padding: 0% 1%;
        }
        @keyframes example {
            0%   {background-color: black;
                  visibility:hidden;
            }
        }
        .movie-tile:hover {
            border : 1px none #444;
            opacity : 0.9;
            background-color : #363636;

        }
        .navbar-brand {
            padding : 0%;

        }
        a:hover {
            color:lightblue;
        }
        .foot {
            background-color: #303030;
        }           
    </style>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body style="background-color:#444;color:#fff;">
  <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>   
    <!-- Main Page Content -->
    <div class="sticky-top">
    <div style="margin-bottom:2%;width:100%;">
        <nav class="navbar navbar-light bg-dark">
            <a class="navbar-brand" href="NoticeApp.html"><p class="load text-light navhead" style="font-weight:bold;">Student Notice Board</p></a>
            <ul class="navbar-nav">
                <li class="nav-item active"><a class="nav-link text-white" href="index.html">Home <span class="sr-only">(current)</span></a></li>
            </ul>    
        </nav>
    </div>
    </div>    
    <div class="container-xs">
    <div class="row">
      {tiles}
    </div>
    <blockquote class="blockquote text-center">
        <code class="mb-0" style="color:#808080;">The distinction between past, present and future is a stubbornly persistent illusion.</code>
        <footer class="blockquote-footer"><cite title="Source Title">Albert Einstein</cite></footer>
    </blockquote>
    </div>
    <div class="row foot">
        <div class="col-sm-6">
             <footer style="margin-top:20px;" class="page-footer font-small blue">
            <div class="footer-copyright text-center py-3"><p class="load">© 2020 Copyright</p>
                <button class="btn btn-dark btn-sm"><a href = "mailto:harshavardhan1830.hv@gmail.com?subject=USER FEEDBACK&body=MENTION YOUR NAME AND ROLLNO THEN START WRITING MAIL.">Send Feedback</a></button>
            </div>
            </footer>
        </div>
        <div class="col-sm-6">
             <footer style="margin-top:20px;" class="page-footer font-small blue">
            <div class="footer-copyright text-center py-3"><p class="load text-">Important Links</p>
                <a href="https://www.mrceterp.com/Login.aspx" target="_blank"><p class="text-primary">MRCET Student Login</p></a>
                <a href="https://mrcet.com/" target="_blank"><p class="text-primary">MRCET Portal</p></a>
            </div>
            </footer>
        </div>
      </div>
  </body>
</html>
'''

# A single movie entry html template
tile_content = '''
<div class="col-lg-3 col-md-4 col-6 movie-tile text-center" style="margin-bottom:2%;">
    <br>
    <a href="{link}" target="_blank"><img src="{image_url}" width="200" height="150" alt="Image"></a>
    <h2>{title}</h2>
    <p>{description}</p>
    <pre style="color:#fff;">Date: {da_te}</pre>
</div>'''

def create_tiles_content(collection):
    # The HTML content for this section of the page
    content = ''
    for collect in collection:
        # Append the tile for the movie with its content filled in
        content += tile_content.format(
            title=collect.title,
            description=collect.description,
            image_url=collect.image_url,
            link=collect.link,
            da_te=collect.da_te
        )
    return content

def open_page(collection):
    # Create or overwrite the output file
    output_file = open('NoticeApp.html', 'w')

    # Replace the placeholder for the movie tiles with the actual dynamically generated content
    rendered_content = main_page_content.format(tiles=create_tiles_content(collection))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser
    url = os.path.abspath('index.html')
    webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
