(defun parse-input (str)
  (mapcar (lambda (x) (split-string x "\n")) (mapcar #'string-trim (split-string (string-trim str) "\\$"))))

(defun parse-cd (cd tree)
  (let ((new-dir (cadr (split-string cd " "))))
    (cond
     ((string= new-dir "..") (cons (cdar tree) (cdr tree)))
     ('t (cons (cons new-dir (car tree)) (cdr tree))))))

(defun parse-ls (ls tree)
  )

(defun parse-command (command tree)
  (cond
   ((string-match-p "ls" (car command)) (parse-ls (cdr command) tree))
   ((string-match-p "cd" (car command)) (parse-cd (car command) tree))))

(let ((input (parse-input (f-read "example"))))
  input)
