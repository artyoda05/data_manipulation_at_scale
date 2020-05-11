SELECT SUM(a.count * b.count) FROM (
    SELECT docid, term, count
    FROM frequency
    WHERE docid = '10080_txt_crude'
) a,
(
    SELECT docid, term, count
    FROM frequency
    WHERE docid = '17035_txt_earn'
) b
WHERE a.term = b.term
ORDER BY a.docid, b.term;