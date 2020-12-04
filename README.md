# koku-web-scraper
Showing the use of Beautiful Soup and Selenium in Python to extract data from the koku site

I was extracting items from an old website where the header tag `<h2>` was the item category while the text underneath were all the items as `<p>`

# Example 

```
<h2>Title</h2>

<p>・item1 ・item2 ・item3 ・item4 ・item5 </p>

```

# Trickiness

All the items were all in one `<p>` so i had use strip to split them up based on the bullet point

```
 elif i.name == 'p':

                dot = " ・"

                value = str(i.text.strip()).split(dot)
                items_list = []
                for j in value:
```
