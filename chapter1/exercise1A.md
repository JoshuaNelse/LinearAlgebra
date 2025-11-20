Exercises 1A
1 Show that 𝛼 + 𝛽 = 𝛽 + 𝛼 for all 𝛼, 𝛽 ∈ 𝐂.
^ use commutativity - field order doesn't matter
2 Show that (𝛼 + 𝛽) + 𝜆 = 𝛼 + (𝛽 + 𝜆) for all 𝛼, 𝛽, 𝜆 ∈ 𝐂.
^ use associativity - operation order doesn't matter
3 Show that (𝛼𝛽)𝜆 = 𝛼(𝛽𝜆) for all 𝛼, 𝛽, 𝜆 ∈ 𝐂.
^ use associativity again
4 Show that 𝜆(𝛼 + 𝛽) = 𝜆𝛼 + 𝜆𝛽 for all 𝜆, 𝛼, 𝛽 ∈ 𝐂.
^ use distributive property
5 Show that for every 𝛼 ∈ 𝐂, there exists a unique 𝛽 ∈ 𝐂 such that 𝛼 + 𝛽 = 0.
^ use additive inverse
6 Show that for every 𝛼 ∈ 𝐂 with 𝛼 ≠ 0, there exists a unique 𝛽 ∈ 𝐂 such that 𝛼𝛽 = 1.
^ use multiplicative inverse
7 Show that (−1 + √3𝑖)/2 is a cube root of 1 (meaning that its cube equals 1).
^ use the above rules to solve (n*n*n) with a complex quotient
8 Find two distinct square roots of 𝑖.
^ not sure actually
9 Find 𝑥 ∈ 𝐑4 such that (4, −3, 1, 7) + 2𝑥 = (5, 9, −6, 8).
R^4 is a field and can be operated on as such (addition across the list) - solve algebraically  
10 Explain why there does not exist 𝜆 ∈ 𝐂 such that 𝜆(2 − 3𝑖, 5 + 4𝑖, −6 + 7𝑖) = (12 − 5𝑖, 7 + 22𝑖, −32 − 9𝑖).
^ has to do with 𝜆 taking the shape (a+bi) I think? might try to solve algebraically to find a false statement
11 Show that (𝑥 + 𝑦) + 𝑧 = 𝑥 + (𝑦 + 𝑧) for all 𝑥, 𝑦, 𝑧 ∈ 𝐅𝑛
^ use associativity for fields (can't remember if they look different from complex numbers or not)

12 Show that (𝑎𝑏)𝑥 = 𝑎(𝑏𝑥) for all 𝑥 ∈ 𝐅𝑛 and all 𝑎, 𝑏 ∈ 𝐅.
^ use associativity

13 Show that 1𝑥 = 𝑥 for all 𝑥 ∈ 𝐅𝑛
^ Multiplicative identity for fields
14 Show that 𝜆(𝑥 + 𝑦) = 𝜆𝑥 + 𝜆𝑦 for all 𝜆 ∈ 𝐅 and all 𝑥, 𝑦 ∈ 𝐅𝑛
^ distributive property for fields
15 Show that (𝑎 + 𝑏)𝑥 = 𝑎𝑥 + 𝑏𝑥 for all 𝑎, 𝑏 ∈ 𝐅 and all 𝑥 ∈ 𝐅^n
^ distributive property for fields


1 Show that 𝛼 + 𝛽 = 𝛽 + 𝛼 for all 𝛼, 𝛽 ∈ 𝐂.

Given C = {c + di | c, d, e, f ∈ R} we can suppose:

a + b = (c + di) + (e + fi)
   ... = c + e + (d+f)i

and:

b + a = (e + fi) + (c + di)
   ... = e + c + (f + d)i

e+c+(f+d)i = c+e+(d+f)i shows via the commutativity of real numbers (R) that a+b = b+a

2 Show that (𝛼 + 𝛽) + 𝜆 = 𝛼 + (𝛽 + 𝜆) for all 𝛼, 𝛽, 𝜆 ∈ 𝐂.

suppose:
    𝛼 = a + bi, 
    𝛽 = c + di, 
    𝜆 = e + fi

((a + bi) + (c + di)) + (e + fi) = (a + bi) + ((c + di) + (e + fi))
((a + c) + (b + d)i) + (e + fi) = (a + bi) + (( c +e) + (d + f)i)

(a+c+e) + (b+d+f)i = (a+c+e) + (b+d+f)i which implies (𝛼 + 𝛽) + 𝜆 = 𝛼 + (𝛽 + 𝜆)

3 Show that (𝛼𝛽)𝜆 = 𝛼(𝛽𝜆) for all 𝛼, 𝛽, 𝜆 ∈ 𝐂.

suppose:
    𝛼 = a + bi,
    𝛽 = c + di,
    𝜆 = e + fi


(𝛼𝛽)𝜆 = ((a + bi) * (c + di)) * (e + fi)
      = ((ac - db) + (adi + cbi)) * (e + fi)
      = ace + acfi - dbe + dbfi + adei - adf + cbei - cbf
      = (ace - dbe - adf - cbf) + (acf +dbf + ade + cbe)i

𝛼(𝛽𝜆) = (a + bi) * ((c + di) * (e + fi))
      = (a + bi) * ((ce - fd + (cfi + edi))
      = ace - afd + acfi + aedi + cebi - fdbi - bcf - bed
      = (ace - afd -bcf - bed) + (acf + aed + ceb + fdb)i

(αβ)λ = ((a + bi)(c + di))(e + fi)
= ((ac - bd) + (ad + bc)i)(e + fi)
= (ac - bd)e + (ac - bd)fi + (ad + bc)ei - (ad + bc)f
= (ace - bde - adf - bcf) + (acf - bdf + ade + bce)i

α(βλ) = (a + bi)((c + di)(e + fi))
= (a + bi)((ce - df) + (cf + de)i)
= a(ce - df) + a(cf + de)i + bi(ce - df) - b(cf + de)
= (ace - adf - bcf - bde) + (acf + ade + bce - bdf)i

therefore (𝛼𝛽)𝜆 = 𝛼(𝛽𝜆)

4 Show that 𝜆(𝛼 + 𝛽) = 𝜆𝛼 + 𝜆𝛽 for all 𝜆, 𝛼, 𝛽 ∈ 𝐂.
