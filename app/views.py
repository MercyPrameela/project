from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def mercy(request):
    return HttpResponse("im god's child")

def me(request):
    return HttpResponse("Hai this is mercy")

def func(request):
    return HttpResponse("<h1>Good Morning</h1>")

def func1(request):
    return HttpResponse("<i>Honey</i>")

def func2(request):
    return HttpResponse("<b>Prameela</b><marquee>akumalla</marquee>")

def func3(request):
    return HttpResponse('<marquee>Cross<img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBwgHBgkIBwgKCgkLDRYPDQwMDRsUFRAWIB0iIiAdHx8kKDQsJCYxJx8fLT0tMTU3Ojo6Iys/RD84QzQ5OjcBCgoKDQwNGg8PGjclHyU3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3Nzc3N//AABEIAJQAlAMBIgACEQEDEQH/xAAcAAABBQEBAQAAAAAAAAAAAAAEAAECAwUHBgj/xAA7EAABBAEDAgMDCAgHAAAAAAABAAIDEQQSITEFQSJRsRNhoQYUMnGBkbLBByMlNENTYnMVJDNCRHJ0/8QAGQEAAwEBAQAAAAAAAAAAAAAAAgMEAQUA/8QAJBEAAgICAgICAwEBAAAAAAAAAAECEQMSITEEEzJhFCJBUQX/2gAMAwEAAhEDEQA/APANYrmMUWXfCvYL5U7OhGiUbUVC0qEbEVE2kiZTBF8LaR0KHhai2lsbS+Rwaxosk9lLMsjwXtUwSsvH+UHR5cn5uzqEJk2Avg32B4K2xElyi4/JBxnGXxZRVpewLkYyFXsipDsa0BwYwbyFbPENGwRWhM5l88LNuQTEdCdyDRQLpN6BshegyWMYwmuy89kN0u1MG17qrE9hGXgdzyRRUa7AKEZL3CuVoQ47xTi1Nf6il+wILCtjYXHZWTR25XYsXhscoW+LCUeaBXNe1xFJLXGMCLdykg9iC0OftarWcog44AB3VThpNK5NPohacewqKvNXMc21nB5CmyU3ax4rCWejbhcKUesEHoeeL5x3/hKAjya8k/U8gO6VltvmF4+CU8NSTKPyE4tHOenUeoYwI2MrPxBd38K4PgO05uO7ylafiF2h2W2j4gveZByoR/zpJKVmk144V7DZWNHPZu0fjTWaXPljo6e1h7QCrBFaaFoO6K0ikhs82ZOY1rWkFYeV3Gnf3BbHVHEE+SypnB/HKuwppWJyNEMLHafER9h7LWZECNvgs2N1EeJFNy9J0gWtyKTZkGkiM2M5ri4WQp47g3Yjf4pjlPcd6A8k4eA4OoWVlOuTbQYBQFp1Frw5oJ8k6TTCs8Y9w0BBS8qcryh3Ek7rqwjRzss7EFMN5Vak1yaTD8FQznfs/JAP8J3opKrM/csj3xu9F4yzxEBqaM/1D1XTWyPGy5gw04HyIXUnsFGvNZkC8f8AtBeNKdrWzhmyFgwsoXa0cXJLSBShzQvo6eGddnp8bgfUiLpAYMupoPuCP2Itc5rkpZldXxyGF97Lz7tfIGy9VmO1N0EWEC5jTEWFgF+e9KvFPVCZw2MQMOkE8lXxQlzNSuOPZofRRTYvAGNCbKQuMSiLHBB1HdTbDRpaLMcBvG9Jm4xB4SdxlA7GeHhJHCA1wkg2PHLG5Dq3Xn+odby2Zb2MEYax1UW3a12oLK6RjZD3PBexztyQe67eqRxHKTBsf5QEbTw/aw/ktHH6zhSUPa6D5PFfHhZMvQZ2/wClKx/uNgoKfp+XBeuB9eY3C9wDcke2ic2VodGQ5vmDaqzh/k5v7bvReHjlkiNxSPYf6XUjG9YzfZOifNra5unxiz96yg/Yq5AAupMf4tLRf1rlhXQMfrWBlEFmQxriPov8J+KyasLBJJuzb2a4eJHYlXdLJgf7TSWuDm+YNha2A2yO9qTJwjo4nbN3DIaK7I5r7CzWECkUxxCglGysKLA8boHLZpdtwUbG7ZQnAcNwvR4BYBGy+yKjiDXC0zGVwio2E8o2wLotZGNle2EKMbCETGEvVmbFYgHkkigQks0YOxwZrdlNoU2tJNkKwRHsu7scrUaOPUrmQn3pRto7oyI3tSBsdBX2Ay9PgyAfbQsd9YBKyuo/J3FGNNNDrjcxhcADYP3r10cbXcBV9Txq6dlGq/VO9Ev2U6GvCmrOUFHZHSOoY+8uJLXm0ah8EB2XWhHQ2CdOWpJixKdnLYMnIxH3BLJE699JI+8Lc6f8s+rYZHijnaOfas3+8UvYS4GNlbZONFJ/2YEHN8jel5A/VCWB3mx9j7ilvJB/JDlgyx5gyfT/ANI2LJpbn4csRG2qN2sfkV7no+fi9Vw48zCkL4X2AS0g2DRXMcj9H2TrBxc6FzL4lBaQPsu/gvf/ACU6ceh9JhwXTCZ0eol4bQ3JP5qTPDFVw7KsE821ZOj0bI7VrYR3VLJrpG41E+JSpMobKhi91IRlvbZaLWjhqZ8Tq3GybCFiHMC1DzUvagDlNNjkbt4Qzmu4T1hFPKEGZJC+zd70kf44HuRyJjiKRDXEjilS0K5uypEImwWd0U2gNgQqoKLlq40DJQNaCUq7H44OXQNCXdgrc95d0rKv+S70KPhwQ0ki6Pmqup4+jpeZtsIXehSd4yfA/SUYuzi67Z818IK4n2XeI3NocUm+RfFE3htc2CNxT5K+OAhGR6XK9sQUjsvTQJHGbRkMdchTbG2+EQ1ra2S2bYzNkTC46hXdVtZaIhiWAM08eu6JcRo5tAMfoFKRnFVaLEuRM+icjhpI7oagnu+6S6sIpI505Nsah5JJ6SRizi8DS5w227ooRh0gDQgWSkNobK6KdzCO6U0yqDia0cDG+La0bikDnZYwle5t9lJuQ8EbnZJcGylZlHpHpvnDGaRdmkH1jKD+lZjW8mF4+CyvnLyNyh86U/Mcjf8AhO9EMcKTs2fk2qOZ9l26KUaG/UuIrrsch0t39yfkVkeCVWbcUwFbouOYWsOJ523R0JJpIlFFkZNmsx4REbmnZZ0YcdgETHFJ3tJdDOTTiAPcIuNouln47H+9HwWPpJUkjS10F7god8ZB2KMEgUHhruCnYFzQjK3QOy+6sSDQFIBdGPRz5djJKVJLQThLSrWGlWArGBA2OQUyQhtWiMfQ5x9pwhGBERtQMaiyRgBtn0UNm/uOT/ad6ItjHeSbPh/Z+SQP4TvRes2Ue2cv7LrUTba36lyVdkx4Tobt2HotmKwK2x4mnZaOMx21BVwRgVYWjAAK2pTTkXwhQTiNd5LUgaK3agYH6eyOiyAOQpXFt8DLSC2tjASdXZViZrq2UwwHdPxYX/SbJk/wjpJ4KQYRyVa1tKRrzVcYJEc5yZWBSmBsnpOmiiNJJ7TL1nqZxJkYVrYgq4yiYqSWyxJMnHDZpFxY6WMW+0AOwWhE25CG8JcpND4QTRXDiE9vgrOo4RHScx1cQPPHuWljNqgeVd1bboXUP/LJ+Eqf2S2Q5wios+fuy+isfpjNDbaeB6L51X1FEdUcZF/RHZU+Qroh8V1YCzpsHewr/mMbWeDdFhjTyVaxgApBHFfYc87XRmexLeArY4pDsQtHS3yTgCuE5YkhEs8mCsgceQrxHp/3KxKkyqFbNlJocvI+tU+0N7G1bOwuO3CrGPXGyTJ0Ph0WskNcWrA8eSHDJmnYbJ9cw4isLNvs3X6CvD5hJDe1f/JSRbfYOn0cbjaNGrvdIhmwBCSSwci+Le7K1oGjbc9u6SSnkyiCD2ktfso9Ze7/AALP3/47/wAJSSQLtDJ/FnCV9O4kzjjRXX0B6BJJXZFyjl4nSYWw6uQFcBQTJLV0DPsknSSRix06SSFmoYcpyAE6SWx6YySSSAKxkkkkVA2z/9k=" alt="pic not found"/></marquee>')