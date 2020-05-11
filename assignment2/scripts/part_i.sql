SELECT * FROM frequency
UNION
SELECT 'q' AS docid, 'washington' AS term, 1 AS count 
UNION
SELECT 'q' AS docid, 'taxes' AS term, 1 AS count
UNION 
SELECT 'q' AS docid, 'treasury' AS term, 1 AS count

SELECT A.docid, B.docid, sum(A.count * B.count) AS similarity 
FROM view_1  A, view_1 B ON A.term = B.term  
WHERE A.docid = 'q' AND B.docid != 'q'
GROUP BY A.docid, B.docid
ORDER BY similarity DESC LIMIT 10;