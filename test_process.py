from process import *
import arrow

def test_condense_busytimes():
    #tests no condensing
    input = [{'desc': '(no description)', 'id': 'ks7dd211cq77n24uis6puk6bu8', 'output_end_time': '11:00', 'output_start_time': '08:00', 'start_date': '2016-12-12T08:00:00-08:00', 'end_date': '2016-12-12T11:00:00-08:00', 'output_date': '2016-12-12', 'summary': 'asdf 1'},
            {'desc': '(no description)', 'id': '7fkhi3vmvn699k2n7agsjpu4q8', 'output_end_time': '16:30', 'output_start_time': '12:00', 'start_date': '2016-12-12T12:00:00-08:00', 'end_date': '2016-12-12T16:30:00-08:00', 'output_date': '2016-12-12', 'summary': 'asdf 2'}]
    expected_output = [{'start_time': '0001-01-01T08:00:00+00:00', 'end_time': '0001-01-01T11:00:00+00:00', 'date': '2016-12-12'}, {'start_time': '0001-01-01T12:00:00+00:00', 'end_time': '0001-01-01T16:30:00+00:00', 'date': '2016-12-12'}]
    output = condense_busytimes(input)
    assert(adjust(output) == expected_output)

    #tests condensing event that starts and ends within another event
    input = [{'desc': '(no description)', 'id': 'un0ugp82cvvf9cmoiat34v4lgk', 'output_end_time': '14:00', 'output_start_time': '13:00', 'start_date': '2016-12-15T13:00:00-08:00', 'end_date': '2016-12-15T14:00:00-08:00', 'output_date': '2016-12-15', 'summary': 'asdf8'}, {'desc': '(no description)',
            'id': '5csj7l3kjlivauebvdcrv0uerg', 'output_end_time': '14:30', 'output_start_time': '12:30', 'start_date': '2016-12-15T12:30:00-08:00', 'end_date': '2016-12-15T14:30:00-08:00', 'output_date': '2016-12-15', 'summary': 'asdf10'}]
    expected_output = [{'start_time': '0001-01-01T12:30:00+00:00', 'end_time': '0001-01-01T14:30:00+00:00', 'date': '2016-12-15'}]
    assert(adjust(condense_busytimes(input)) == expected_output)

    #tests condensing event that overlaps with another event
    input = [{'desc': '(no description)', 'id': '1oj6pnevf2532p1gris55iotn4', 'output_end_time': '14:00', 'output_start_time': '12:00', 'start_date': '2016-12-16T12:00:00-08:00', 'end_date': '2016-12-16T14:00:00-08:00', 'output_date': '2016-12-16', 'summary': 'adsf'}, {'desc': '(no description)',
            'id': '97uudcc7f3uu3mkeeqa9qtdr1c', 'output_end_time': '15:00', 'output_start_time': '12:30', 'start_date': '2016-12-16T12:30:00-08:00', 'end_date': '2016-12-16T15:00:00-08:00', 'output_date': '2016-12-16', 'summary': 'asdf2'}, {'desc': '(no description)', 'id': 'mjcktk80i3brc276tiaf0bvp7s', 'output_end_time': '16:00', 'output_start_time': '15:00', 'start_date': '2016-12-16T15:00:00-08:00', 'end_date': '2016-12-16T16:00:00-08:00', 'output_date': '2016-12-16', 'summary': 'afsafdsfa'}, {'desc': '(no description)', 'id': 'ggg8kvek0cvvpq830i0l2khh94', 'output_end_time': '17:30', 'output_start_time': '16:30', 'start_date': '2016-12-16T16:30:00-08:00', 'end_date': '2016-12-16T17:30:00-08:00', 'output_date': '2016-12-16', 'summary': 'hhjadfsadjksfh'}]
    expected_output = [{'start_time': '0001-01-01T12:00:00+00:00', 'end_time': '0001-01-01T16:00:00+00:00', 'date': '2016-12-16'}, {'start_time': '0001-01-01T16:30:00+00:00', 'end_time': '0001-01-01T17:30:00+00:00', 'date': '2016-12-16'}]
    assert(adjust(condense_busytimes(input)) == expected_output)

    return

def test_free_time():
    return

def adjust(events):
    for event in events:
        old_start = event['start_time']
        old_end = event['end_time']
        event['start_time'] = str(old_start)
        event['end_time'] = str(old_end)
    return events