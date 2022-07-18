#List of common keyboard strokes for programmers

# Initiate dcitionary of lists with syntax sets. Default is syntax
list_ = {"syntax": 
            [ "*","(",")","_","+",
            "{","}","|","[","]","\\",
            ":",'"',"'",";","'",
            "<",">","?",",",".","?",
            "%","#","!","~","`","^","&" 
            ],

        #Common git Commands            
        "git" :
            ["cd","cd ~","cd ../","ls","pwd"
            "touch","echo","mkdir", "git add .",
            "git commit -m", "git push", "git clone",
            "git checkout", "git pull", "code", "python",
            "jupyter lab","conda activate","cp", "git status",
            "git diff", "git config", "git init", "git branch",
            "git log", "git merge", "git log", "git show",
            "git fetch", "git remote add", "git rebase", "git rm",
            "git mv", "git log", "git reset", "git rebase", "git stash"
            ],
        
        # Common python functions
        "python":
            ["if","elif","else","for","break",
            "and","or","len","input", "range", "in",
            "str", "int","float", "tuple", "type",
             "is" , "is not" ,"True","False", "add", "lambda",
             "pass","while", "print", "from", "import",
             "def", "return" , ".pop","reverse", "set", ".remove",
             ".update", ".discard", ".union", ".intersection", "difference",
             "del","zip", ".values" , ".get", ".setdefault",
             "+=", "-=","*=","/=","%=","==", "!=", "<=", ">=",
             ".append",".insert",".remove",".sort","sorted()", "list",
             "end", "sep" , ".format"
            ],
        
        #Common PANDAS functionality
        "pandas":
            ["loc","iloc", "df",
            ".read_csv" ,".read_table" ,".read_excel" ,".read_sql",
            ".read_json" ,".read_html" ,".read_clipboard", ".DataFrame",
            ".to_csv", ".to_excel", ".to_sql", ".to_json"
            ".Series",".index=",".DataFrame",".columns",
            ".head", ".tail",".shape",".info",".describe",".value_counts",".apply",
            ".isnull" ,".notnull" ,".dropna" ,".fillna" ,".astype" ,".replace" ,
            ".rename" ,".set_index" ,".sort_values" ,".sort_index" ,
            ".groupby" ,".pivot" ,".apply" ,".append" ,".concat" , ".join",
            ".describe" ,".mean" ,".corr" ,".count" ,".max" ,
            ".min" ,".median" ,".std" 
            ]
        }