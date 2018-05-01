import datetime, re

address = 'path'

def add_day_progress_thoughts(progress,thoughts):
    with open(address, mode='a+') as file:
        file.seek(0)
        content = file.read()
        i = content.rfind('### Day ')
        day_no = int(re.sub('\D',"",content[i+8: i+11]))+1
        date = datetime.datetime.now()
        date_str = date.strftime('%B %d, %Y')
        output_str = '\n### Day %s: %s\n\n**Today\'s Progress**: %s\n\n**Thoughts**: %s\n\n' % (str(day_no),date_str,progress,thoughts)
        file.write(output_str)

def add_links(link_names,links):
    output_str = '**Links to projects**: \n'
    for name, link in zip(link_names,links):
        output_str += '[%s](%s)\n' % (name,link)
    with open(address, mode='a+') as file:
        file.write(output_str)
