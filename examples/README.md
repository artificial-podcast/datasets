## Tests

Search term:

https://archiveofourown.org/works?utf8=%E2%9C%93&work_search%5Bsort_column%5D=revised_at&include_work_search%5Bfreeform_ids%5D%5B%5D=55907&include_work_search%5Bfreeform_ids%5D%5B%5D=123409&work_search%5Bother_tag_names%5D=&exclude_work_search%5Bfandom_ids%5D%5B%5D=27&exclude_work_search%5Bfandom_ids%5D%5B%5D=13999&exclude_work_search%5Bfandom_ids%5D%5B%5D=115613&exclude_work_search%5Bfandom_ids%5D%5B%5D=133185&exclude_work_search%5Bfandom_ids%5D%5B%5D=232768&exclude_work_search%5Bfandom_ids%5D%5B%5D=414093&exclude_work_search%5Bfandom_ids%5D%5B%5D=1001939&exclude_work_search%5Bfandom_ids%5D%5B%5D=22001796&exclude_work_search%5Brelationship_ids%5D%5B%5D=99&exclude_work_search%5Brelationship_ids%5D%5B%5D=1600&exclude_work_search%5Brelationship_ids%5D%5B%5D=2390&exclude_work_search%5Brelationship_ids%5D%5B%5D=3458&exclude_work_search%5Brelationship_ids%5D%5B%5D=3548&exclude_work_search%5Brelationship_ids%5D%5B%5D=20822&exclude_work_search%5Brelationship_ids%5D%5B%5D=163914&work_search%5Bexcluded_tag_names%5D=&work_search%5Bcrossover%5D=&work_search%5Bcomplete%5D=T&work_search%5Bwords_from%5D=20000&work_search%5Bwords_to%5D=&work_search%5Bdate_from%5D=&work_search%5Bdate_to%5D=&work_search%5Bquery%5D=&work_search%5Blanguage_id%5D=en&commit=Sort+and+Filter&tag_id=Hermione+Granger


Create the reference training set:

```shell
cd examples/datasets

# v1
apc 24304135 .
apc 30390987 .
apc 31265246 .
apc 31834528 .
apc 32797090 .
apc 34259563 .
apc 36609685 .
apc 37087273 .

# v2
apc 28339248 .
apc 31014302 .
apc 31099430 .
apc 33148525 .
apc 32975227 .
apc 31433078 .
apc 28610865 .
apc 23994118 .
apc 28742985 .
apc 30360807 .
apc 28979823 .
apc 29539653 .
apc 29327319 .
apc 26828773 .
apc 22287295 .
apc 15370968 .
apc 22249729 .
apc 24707470 .
apc 13553997 .
apc 13774476 .
apc 10857801 .
apc 8850352 .
apc 4201809 .
apc 2797229 .
apc 3704107 .
apc 896640 .
apc 384316 .
apc 10812861 .
apc 10804995 .
apc 10799067 .
apc 10814574 .
apc 10798827 .
apc 10814298 .
apc 10814817 .
apc 10814796 .
apc 10814559 .
apc 10814484 .

cd ..

python -m texttools.merge examples

```
