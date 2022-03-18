## Examples

Search for texts with e.g. the following search term:

```
https://archiveofourown.org/works?utf8=%E2%9C%93&work_search%5Bsort_column%5D=revised_at&include_work_search%5Bfreeform_ids%5D%5B%5D=55907&include_work_search%5Bfreeform_ids%5D%5B%5D=123409&work_search%5Bother_tag_names%5D=&exclude_work_search%5Bfandom_ids%5D%5B%5D=27&exclude_work_search%5Bfandom_ids%5D%5B%5D=13999&exclude_work_search%5Bfandom_ids%5D%5B%5D=115613&exclude_work_search%5Bfandom_ids%5D%5B%5D=133185&exclude_work_search%5Bfandom_ids%5D%5B%5D=232768&exclude_work_search%5Bfandom_ids%5D%5B%5D=414093&exclude_work_search%5Bfandom_ids%5D%5B%5D=1001939&exclude_work_search%5Bfandom_ids%5D%5B%5D=22001796&exclude_work_search%5Brelationship_ids%5D%5B%5D=99&exclude_work_search%5Brelationship_ids%5D%5B%5D=1600&exclude_work_search%5Brelationship_ids%5D%5B%5D=2390&exclude_work_search%5Brelationship_ids%5D%5B%5D=3458&exclude_work_search%5Brelationship_ids%5D%5B%5D=3548&exclude_work_search%5Brelationship_ids%5D%5B%5D=20822&exclude_work_search%5Brelationship_ids%5D%5B%5D=163914&work_search%5Bexcluded_tag_names%5D=&work_search%5Bcrossover%5D=&work_search%5Bcomplete%5D=T&work_search%5Bwords_from%5D=20000&work_search%5Bwords_to%5D=&work_search%5Bdate_from%5D=&work_search%5Bdate_to%5D=&work_search%5Bquery%5D=&work_search%5Blanguage_id%5D=en&commit=Sort+and+Filter&tag_id=Hermione+Granger
```


Create the reference training set:

```shell
cd examples

apc 384316 .
apc 896640 .

cd ..

python -m texttools.merge examples

```
